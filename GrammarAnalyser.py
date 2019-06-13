from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

from MainWindow import Ui_MainWindow, Ui_DialogWords, Ui_DialogHowToUse, Ui_DialogAboutAuthor, Ui_DialogAboutGrammarAnalyser
from HtmlFormatter import HtmlFormatter, Html
from utils.Notification import NotificationWindow

import os
import sys

from cmp.grammartools import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNewGrammar.triggered.connect(self.new_grammar)
        self.ui.actionLoadGrammar.triggered.connect(self.load_grammar)
        self.ui.actionSaveGrammar.triggered.connect(self.save_grammar)
        self.ui.actionSaveGrammarAs.triggered.connect(self.save_grammar_as)
        self.ui.actionAnalyse.triggered.connect(self.show_words_dialog)
        self.ui.actionQuickAnalyse.triggered.connect(self.quick_analyse_grammar)
        self.ui.actionExit.triggered.connect(self._exit)
        self.ui.actionHowToUse.triggered.connect(self.how_to_use)
        self.ui.actionAboutAuthor.triggered.connect(self.about_author)
        self.ui.actionAboutGrammarAnalyser.triggered.connect(self.about_grammar_analyser)
        
        self.new_grammar()


    def clear_results(self):
        self.ui.tabWidget.setTabEnabled(1, False)
    
    def update_status(self):
        self.ui.tabWidget.setStatusTip(self.path if self.path else "*Nueva Gramática")
        # self.ui.statusbar.showMessage(self.path if self.path else "")

    def new_grammar(self):
        self.path = None
        self.ui.textEditGrammar.setPlainText("")
        self.update_status()
        self.clear_results()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def load_grammar(self):
        path, _ = QFileDialog.getOpenFileName(self, "Cargar Gramática", "", "Documentos de texto (*.txt)")

        if not path:
            # If dialog is cancelled, will return ''
            return

        try:
            with open(path, 'r') as f:
                text = f.read()

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.ui.textEditGrammar.setPlainText(text)
            self.update_status()
            self.clear_results()

    def save_grammar(self):
        if self.path is None:
            # If we do not have a path, we need to use Save As.
            return self.save_grammar_as()

        text = self.ui.textEditGrammar.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

    def save_grammar_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Guardar Gramática", "", "Documentos de texto (*.txt)")
        text = self.ui.textEditGrammar.toPlainText()

        if not path:
            # If dialog is cancelled, will return ''
            return

        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_status()

    def _exit(self):
        self.close()

    def show_words_dialog(self):
        self.ui_dialog = Ui_DialogWords()
        dialog = QDialog()
        self.ui_dialog.setupUi(dialog)

        dialog.accepted.connect(self.normal_analyse_grammar)
        self.ui_dialog.wordsText.setFocus()

        dialog.exec()

    def normal_analyse_grammar(self):
        return self.analyse_grammar(self.ui_dialog.wordsText.toPlainText().split('\n'))

    def quick_analyse_grammar(self):
        return self.analyse_grammar()
    
    def analyse_grammar(self, words=[]):
        text = self.ui.textEditGrammar.toPlainText()

        try:
            grammar = GrammarTools.grammar_from_text(text)

        except BadTextFormatException:
            NotificationWindow.error('Error', 
                                    '''<html><head/><body><span style=" font-style:italic; color:teal;">
                                    <p>La gamática no está escrita en el formato correcto.</p>
                                    <p>Lea la ayuda de cómo usar Grammar Analyser.</p><p></p>
                                    </span></body></html>''', callback=lambda: self.how_to_use())

        else:
            NotificationWindow.info('Analizando', 
                                    '''<html><head/><body><span style="color:gray;">
                                    <p>La gramática está siendo analizada.</p>
                                    <p>Espere unos instantes.</p><p></p>
                                    </span></body></html>''')

            words = [GrammarTools.tokenizer(grammar, word) for word in words]
            grammar_clone = GrammarTools.clone_grammar(grammar)
            is_not_null, acepted_symbols = GrammarTools.is_not_null(grammar_clone)
            GrammarTools.remove_bad_items(grammar_clone, keep_symbols=acepted_symbols)
            GrammarTools.remove_left_recursion(grammar_clone)
            GrammarTools.factorize_grammar(grammar_clone)
            firsts = GrammarTools.compute_firsts(grammar)
            follows = GrammarTools.compute_follows(grammar, firsts)
            ll1_table, is_ll1 = GrammarTools.build_ll1_table(grammar, firsts, follows)
            parser, parser_type = None, None
            parser_ll1 = GrammarTools.nonrecursive_predictive_method(grammar, ll1_table, firsts, follows)
            if is_ll1: parser, parser_type = parser_ll1, 'left'
            parser_slr1 = SLR1Parser(grammar)
            if parser_slr1.is_slr1: parser, parser_type = parser_slr1, 'right'
            parser_lr1 = LR1Parser(grammar)
            if parser_lr1.is_lr1: parser, parser_type = parser_lr1, 'right'
            parser_lalr1 = LALR1Parser(grammar)
            if parser_lalr1.is_lr1: parser, parser_type = parser_lalr1, 'right'
            derivations = [parser(word) for word in words] if parser else []
            derivations = [DerivationTree.get_tree(derivation, parser_type)._repr_svg_() if derivation else None for derivation in derivations]
            regular_automaton, is_regular = GrammarTools.build_automaton(grammar) 
            regular_expersion = GrammarTools.regexp_from_automaton(regular_automaton)

            grammar_html = HtmlFormatter.grammar_to_html(grammar)
            is_not_null_html = '' if is_not_null else HtmlFormatter.error_message_to_html("Esta gramática genera el lenguaje: \N{LATIN CAPITAL LETTER O WITH STROKE}")
            grammar_clone_html = HtmlFormatter.grammar_to_html(grammar_clone)
            firsts_html = HtmlFormatter.firsts_to_html(grammar, firsts)
            follows_html = HtmlFormatter.follows_to_html(grammar, follows)
            ll1_table_html = HtmlFormatter.ll1_table_to_html(grammar, ll1_table, 'NoT-T')
            is_ll1_html = HtmlFormatter.good_message_to_html("La gramática es LL(1)") if is_ll1 else HtmlFormatter.error_message_to_html("La gramática no es LL(1)")
            augmented_grammar_html = HtmlFormatter.grammar_to_html(parser_slr1.augmentedG)
            items_collection_lr0_html = HtmlFormatter.items_collection_to_html(parser_slr1.automaton)
            automaton_lr0_html = parser_slr1.automaton._repr_svg_()
            if automaton_lr0_html is None: automaton_lr0_html = HtmlFormatter.error_message_to_html("Imposible mostrar el autómata, ver problemas con el software Graphviz")
            action_slr1_html = HtmlFormatter.action_goto_table_to_html(parser_slr1.action, parser_slr1.G.terminals + [parser_slr1.G.EOF], 'ACTION')
            goto_slr1_html = HtmlFormatter.action_goto_table_to_html(parser_slr1.goto, parser_slr1.G.nonTerminals, 'GOTO')
            is_slr1_html = HtmlFormatter.good_message_to_html("La gramática es SLR(1)") if parser_slr1.is_slr1 else HtmlFormatter.error_message_to_html("La gramática no es SLR(1)")
            items_collection_lr1_html = HtmlFormatter.items_collection_to_html(parser_lr1.automaton)
            automaton_lr1_html = parser_lr1.automaton._repr_svg_()
            if automaton_lr1_html is None: automaton_lr1_html = HtmlFormatter.error_message_to_html("Imposible mostrar el autómata, ver problemas con el software Graphviz")
            action_lr1_html = HtmlFormatter.action_goto_table_to_html(parser_lr1.action, parser_lr1.G.terminals + [parser_lr1.G.EOF], 'ACTION')
            goto_lr1_html = HtmlFormatter.action_goto_table_to_html(parser_lr1.goto, parser_lr1.G.nonTerminals, 'GOTO')
            is_lr1_html = HtmlFormatter.good_message_to_html("La gramática es LR(1)") if parser_lr1.is_lr1 else HtmlFormatter.error_message_to_html("La gramática no es LR(1)")
            items_collection_lalr1_html = HtmlFormatter.items_collection_to_html(parser_lalr1.automaton)
            automaton_lalr1_html = parser_lalr1.automaton._repr_svg_()
            if automaton_lalr1_html is None: automaton_lalr1_html = HtmlFormatter.error_message_to_html("Imposible mostrar el autómata, ver problemas con el software Graphviz")
            action_lalr1_html = HtmlFormatter.action_goto_table_to_html(parser_lalr1.action, parser_lalr1.G.terminals + [parser_lalr1.G.EOF], 'ACTION')
            goto_lalr1_html = HtmlFormatter.action_goto_table_to_html(parser_lalr1.goto, parser_lr1.G.nonTerminals, 'GOTO')
            is_lalr1_html = HtmlFormatter.good_message_to_html("La gramática es LALR(1)") if parser_lalr1.is_lr1 else HtmlFormatter.error_message_to_html("La gramática no es LALR(1)")
            derivations_html = HtmlFormatter.derivations_to_html(words, derivations) if derivations else HtmlFormatter.error_message_to_html("La gramática no es LL(1), ni SLR(1), ni LR(1), imposible obtener las derivaciones") if words else HtmlFormatter.error_message_to_html("No se sleccionó ninguna cadena")
            is_regular_html = HtmlFormatter.good_message_to_html("La gramática es Regular") if is_regular else HtmlFormatter.error_message_to_html("La gramática no es Regular")
            regular_automaton_html = regular_automaton._repr_svg_() if is_regular else HtmlFormatter.error_message_to_html("Imposible obtener autómata, la gramática no es Regular")
            if regular_automaton_html is None: regular_automaton_html = HtmlFormatter.error_message_to_html("Imposible mostrar el autómata, ver problemas con el software Graphviz")
            regular_expersion_html = HtmlFormatter.message_to_html(regular_expersion) if is_regular else HtmlFormatter.error_message_to_html("Imposible obtener expresión, la gramática no es Regular")

            self.ui.tabWidget.setTabEnabled(1, True)
            self.ui.tabWidget.setCurrentIndex(1)
            self.ui.textResults.setHtml(Html % (grammar_html + is_not_null_html, grammar_clone_html,
                                            firsts_html, follows_html, ll1_table_html, is_ll1_html, 
                                            augmented_grammar_html, 
                                            items_collection_lr0_html, automaton_lr0_html, action_slr1_html, 
                                            goto_slr1_html, is_slr1_html,
                                            items_collection_lr1_html, automaton_lr1_html, action_lr1_html, 
                                            goto_lr1_html, is_lr1_html,
                                            items_collection_lalr1_html, automaton_lalr1_html, action_lalr1_html, 
                                            goto_lalr1_html, is_lalr1_html, derivations_html,
                                            is_regular_html, regular_automaton_html, regular_expersion_html))

            NotificationWindow.success('Listo', 
                                    '''<html><head/><body><span style="color:green;">
                                    <p>El análisis de la gramática ha termiando.</p>
                                    <p>Todos los resultados están listos</p><p></p>
                                    </span></body></html>''')

    def how_to_use(self):
        dialog = QDialog()
        ui_dialog = Ui_DialogHowToUse()
        ui_dialog.setupUi(dialog)

        dialog.exec()

    def about_author(self):
        dialog = QDialog()
        ui_dialog = Ui_DialogAboutAuthor()
        ui_dialog.setupUi(dialog)

        dialog.exec()

    def about_grammar_analyser(self):
        dialog = QDialog()
        ui_dialog = Ui_DialogAboutGrammarAnalyser()
        ui_dialog.setupUi(dialog)

        dialog.exec()
        


if __name__ == '__main__':

    # sys.argv.append("--disable-web-security")
    # app = QApplication(sys.argv)
    app = QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
