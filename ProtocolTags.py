import sublime
import sublime_plugin
import random
import string
import datetime

class TemplateTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%dT%H:%M:%S.%f") + "+03:00"
        pos = self.view.sel()[0].begin()
        self.view.insert(edit, pos, """<?xml version="1.0" encoding="utf-8"?>
<ProtocolTemplateModel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<Version>1</Version>
<Id>1</Id>
<Name>Безымянный</Name>
<Created>""" + formatted_date + """</Created>
<FontSize xsi:nil="true" />\n
</ProtocolTemplateModel>""")


class TextboxTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pos = self.view.sel()[0].begin()
        tag_id = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5)))
        snippet = "<TextBox Id=\"" + tag_id + "\" Name=\"\" ItemType=\"TextBox\" IsEnabled=\"true\" IsVisible=\"true\" Value=\"\" IsBoldLabel=\"true\" MinWidth=\"300\" IsRequired=\"true\" Lines=\"1\" />"

        self.view.insert(edit, pos, snippet)

class TextblockTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pos = self.view.sel()[0].begin()
        tag_id = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5)))
        snippet = "<TextBlock Id=\"" + tag_id + "\" ItemType=\"TextBlock\" IsEnabled=\"true\" IsVisible=\"true\" Value=\"\" MinWidth=\"200\" IsBold=\"true\" />"
        
        self.view.insert(edit, pos, snippet)
        
class ComboboxTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pos = self.view.sel()[0].begin()
        tag_id = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5)))
        snippet = "<ComboBox Id=\"" + tag_id + "\" Name=\"\" ItemType=\"ComboBox\" IsEnabled=\"true\" IsVisible=\"true\" IsBoldLabel=\"true\" MinWidth=\"150\" IsRequired=\"true\" Values=\"\" IsTextEditable=\"true\" IsConclusionTemplate=\"false\" IsDictionaryTemplate=\"false\" Multiselect=\"false\" IsSelectedFromNetrika=\"false\" IsUseNetrika=\"false\" />"
        
        self.view.insert(edit, pos, snippet)

class NumericboxTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pos = self.view.sel()[0].begin()
        tag_id = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5)))
        snippet = "<NumericBox Id=\"" + tag_id + "\" Name=\"\" ItemType=\"NumericBox\" IsRequired=\"true\" IsEnabled=\"true\" IsVisible=\"true\" Value=\"\" IsBoldLabel=\"true\" MinWidth=\"85\" Unit=\"\" FormatString=\"N0\" />"
        
        self.view.insert(edit, pos, snippet)

class CheckboxTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pos = self.view.sel()[0].begin()
        tag_id = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5)))
        snippet = "<CheckBox Id=\"" + tag_id + "\" Name=\"\" ItemType=\"CheckBox\" IsEnabled=\"true\" IsVisible=\"true\" MinWidth=\"150\" TextTrue=\"\" TextFalse=\"\" />"
        
        self.view.insert(edit, pos, snippet)
        
class DateTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pos = self.view.sel()[0].begin()
        tag_id = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5)))
        snippet = "<Date Id=\"" + tag_id + "\" Name=\"\" ItemType=\"Date\" IsEnabled=\"true\" IsVisible=\"true\" IsLabelVisible=\"true\" />"
        
        self.view.insert(edit, pos, snippet)
        
class StackpanelTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pos = self.view.sel()[0].begin()
        tag_id = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5)))
        snippet = "<StackPanel Id=\"" + tag_id + "\" Name=\"\" ItemType=\"StackPanel\" IsEnabled=\"true\" IsVisible=\"true\" IsLabelVisible=\"false\" Orientation=\"Horizontal\">\n\t\n</StackPanel>"
        
        self.view.insert(edit, pos, snippet)
        
class mkbTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pos = self.view.sel()[0].begin()
        tag_id = ''.join(random.sample(string.digits, random.randint(1, 1)))
        snippet = "<ComboBox Id=\"MKBDiagnosis" + tag_id + "\" Name=\"Диагноз по МКБ\" ItemType=\"ComboBox\" IsEnabled=\"true\" IsVisible=\"true\" IsBoldLabel=\"true\" MinWidth=\"225\" IsLabelVisible=\"true\" IsPrintableNameIfValueNotNull=\"true\" DataSource=\"MKB\" KeyColumnName=\"Id\" DataColumnName=\"CodeWithName\" IsTextEditable=\"false\" IsConclusionTemplate=\"false\" IsDictionaryTemplate=\"false\" Multiselect=\"true\" IsSelectedFromNetrika=\"false\" IsUseNetrika=\"false\" />"

        self.view.insert(edit, pos, snippet)      
        
class InsertCheckboxEventListener(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if prefix == "chx":
            snippet = "<CheckBox Id=\"" + ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5))) + "\" Name=\"\" ItemType=\"CheckBox\" IsEnabled=\"true\" IsVisible=\"true\" MinWidth=\"150\" TextTrue=\"\" TextFalse=\"\" />"
            return [("chx\tCheckbox", snippet)]
        if prefix == "tbx":
            snippet1 = "<TextBox Id=\"" + ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5))) + "\" Name=\"\" ItemType=\"TextBox\" IsEnabled=\"true\" IsVisible=\"true\" Value=\"\" IsBoldLabel=\"true\" MinWidth=\"300\" IsRequired=\"true\" Lines=\"1\" />"
            return [("tbx\tTextbox", snippet1)]
        if prefix == "cbx":
            snippet2 = "<ComboBox Id=\"" + ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5))) + "\" Name=\"\" ItemType=\"ComboBox\" IsEnabled=\"true\" IsVisible=\"true\" IsBoldLabel=\"true\" MinWidth=\"150\" IsRequired=\"true\" Values=\"\" IsTextEditable=\"true\" IsConclusionTemplate=\"false\" IsDictionaryTemplate=\"false\" Multiselect=\"false\" IsSelectedFromNetrika=\"false\" IsUseNetrika=\"false\" />"
            return [("cbx\tCombobox", snippet2)]
        if prefix == "dt":
            snippet3 = "<Date Id=\"" + ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5))) + "\" Name=\"\" ItemType=\"Date\" IsEnabled=\"true\" IsVisible=\"true\" IsLabelVisible=\"true\" />"
            return [("dt\tDate", snippet3)]
        if prefix == "mkb":
            snippet4 = "<ComboBox Id=\"MKBDiagnosis" + ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5))) + "\" Name=\"Диагноз по МКБ\" ItemType=\"ComboBox\" IsEnabled=\"true\" IsVisible=\"true\" IsBoldLabel=\"true\" MinWidth=\"225\" IsLabelVisible=\"true\" IsPrintableNameIfValueNotNull=\"true\" DataSource=\"MKB\" KeyColumnName=\"Id\" DataColumnName=\"CodeWithName\" IsTextEditable=\"false\" IsConclusionTemplate=\"false\" IsDictionaryTemplate=\"false\" Multiselect=\"true\" IsSelectedFromNetrika=\"false\" IsUseNetrika=\"false\" />"
            return [("mkb\tMKB", snippet4)]
        if prefix == "stc":
            snippet5 = "<StackPanel Id=\"" + ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5))) + "\" Name=\"\" ItemType=\"StackPanel\" IsEnabled=\"true\" IsVisible=\"true\" IsLabelVisible=\"false\" Orientation=\"Horizontal\">\n\t\n</StackPanel>"
            return [("stc\tStackPanel", snippet5)]
        if prefix == "num":
            snippet6 = "<NumericBox Id=\"" + ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5))) + "\" Name=\"\" ItemType=\"NumericBox\" IsRequired=\"true\" IsEnabled=\"true\" IsVisible=\"true\" Value=\"\" IsBoldLabel=\"true\" MinWidth=\"85\" Unit=\"\" FormatString=\"N0\" />"
            return [("num\tNumericBox", snippet6)]
        if prefix == "tbc":
            snippet6 = "<TextBlock Id=\"" + ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5))) + "\"ItemType=\"TextBlock\" IsEnabled=\"true\" IsVisible=\"true\" Value=\"\" MinWidth=\"200\" IsBold=\"true\" />"
            return [("tbc\tTextBlock", snippet6)]
        return []