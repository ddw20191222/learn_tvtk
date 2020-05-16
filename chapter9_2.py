#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-
# software: sublime Text3
# name: chapter9_2.py
# date: 2020.05.16
# website: https://www.icourse163.org/course/BIT-1001871001

__author__="ddw20191222"

from traits.api import HasTraits, Str, Int

class ModelManager(HasTraits):
	model_name = Str
	category = Str
	model_file = Str
	model_number = Int
def test01():
	model = ModelManager()
	model.configure_traits()

from traitsui.api import View, Item

class ModelManager2(HasTraits):
	model_name = Str
	category = Str
	model_file = Str
	model_number = Int
	View = View(
		Item("model_name", label = u"模型名称"),
		Item("model_file", label = u"文件名", tooltip = u"路径及文件名"),
		Item("category", label = u"模型类型"),
		Item("model_number", label = u"模型数量"),
		title = u"模型资料", width = 200, resizable = True		
		)


def test02():
	model = ModelManager2()
	model.configure_traits()


from traitsui.api import Group
class ModelManager3(HasTraits):
	model_name = Str
	category = Str
	model_file = Str
	model_number = Int	
	vertices = Int
view1 = View(
	Group(
		Group(
			Item("model_name", label = u"模型名称"),
			Item("model_file", label = u"文件名", tooltip = u"路径及文件名"),
			Item("category", label = u"模型类型"),
			label = u"模型信息", show_border = True
			),
		Group(
			Item("model_number", label = u"模型数量"),
			Item("vertices", label = u"顶点数量"),
			label = u"统计数据",
			show_border = True	
			)
		)
	)
def test03():
	model = ModelManager3()
	model.configure_traits(view = view1)


def test04():
	model = ModelManager()
	model.edit_traits()


from traitsui.menu import ModalButtons
class ModelManager4(HasTraits):
	model_name = Str
	category = Str
	model_file = Str
	model_number = Int	
	vertices = Int
view1 = View(
	Group(
		Group(
			Item("model_name", label = u"模型名称"),
			Item("model_file", label = u"文件名", tooltip = u"路径及文件名"),
			Item("category", label = u"模型类型"),
			label = u"模型信息", show_border = True
			),
		Group(
			Item("model_number", label = u"模型数量"),
			Item("vertices", label = u"顶点数量"),
			label = u"统计数据",
			show_border = True	
			)
		),
	kind = "modal",
	buttons = ModalButtons
	)
def test05():
	model = ModelManager4()
	model.configure_traits(view = view1)



from traits.api import Password
class TextEditor(HasTraits):
	string_trait = Str("sample string")
	password = Password

	text_str_group = View(
		Group(
			Item("string_trait", style = "simple", label = "Simple"),
			Item("_"),
			Item("string_trait", style = "custom", label = "Custom"),
			Item("_"),
			Item("password", style = "simple", label = "password")
			),
		title = "TextEditor",
		buttons = ["OK"]
		)
def test06():
	text = TextEditor()
	text.configure_traits()



if __name__ == "__main__":
	# test04()
	# test02()
	# test03()
	# test05()
	test06()
