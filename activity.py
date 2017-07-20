import gi
import logging

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox

from sugar3.activity.widgets import(
	ActivityToolbarButton,
	StopButton)


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

logger = logging.getLogger(__name__)

class SistemaSolar(activity.Activity):

	def __init__(self, handle):
		activity.Activity.__init__(self, handle)
		self.agregar_toolbar()

	def agregar_toolbar(self):
		toolbar_box = ToolbarBox()
		activity_toolbar_button = ActivityToolbarButton(self)
		activity_stop_button = StopButton(self)

		toolbar_box.toolbar.insert(activity_toolbar_button, 0)
		activity_toolbar_button.show()

		toolbar_box.toolbar.insert(activity_stop_button, -1)
		activity_stop_button.show()

		description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

		self.set_toolbar_box(toolbar_box)
		toolbar_box.show()

