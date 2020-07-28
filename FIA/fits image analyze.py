from tkinter import *
import matplotlib.pyplot as plt 
from astropy.io import fits
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename

plt.style.use(astropy_mpl_style)


class Main():

	def __init__(self):
		self.root = Tk()
		self.root.title("FIA")

		self.inp_field_color = "#474747"
		self.text_color = "white"
		self.text_dark_color = "black"
		self.frame_dark_color = "#363636"
		self.entry_text_color = "#d4d4d4"
		self.btn_colot_dark = "#8c8c8c"


	def MainFrameWidgets(self):
		self.main_window = Frame(self.root, bg = self.frame_dark_color, height = "400px", width = "600px")
		self.main_window.pack()


		self.side_options_frame = Frame(self.main_window, bg = self.inp_field_color, height = "400px", width = "100px")
		self.side_options_frame.place(x = "0px", y = "0px")


		self.file_options = Button(self.side_options_frame, text = "file options", width = 16, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: frameToggles("file options"))
		self.file_options.place(x = "4px", y = "10px")

		self.inspect_data_frame = Button(self.side_options_frame, text = "inspect data", width = 16, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: frameToggles("inspect data"))
		self.inspect_data_frame.place(x = "4px", y = "30px")

		self.show_histogram_frame = Button(self.side_options_frame, text = "inspect picture", width = 16, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: frameToggles("histogram"))
		self.show_histogram_frame.place(x = "4px", y = "50px")

		self.show_histogram_frame = Button(self.side_options_frame, text = "show histogram", width = 16, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: frameToggles("histogram"))
		self.show_histogram_frame.place(x = "4px", y = "70px")


		self.inspectDataFrame()
		self.fileOptionsFrame()

		
		def frameToggles(frame_name):
			if frame_name == "file options":
				self.fileOptionsFrame()
				self.file_inspect_data_frame.place_forget()

			elif frame_name == "inspect data":
				self.inspectDataFrame()
				self.file_options_frame.place_forget()

			elif frame_name == "histogram":
				self.showHistogram()

		self.root.resizable(0,0)
		self.root.mainloop()


	def fileOptionsFrame(self):
		self.file_options_frame = Frame(self.main_window, bg = self.frame_dark_color, width = "500px", height = "400px")
		self.file_options_frame.place(x = "100px", y = "0px")

		Label(self.file_options_frame, text = "import image", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "10px")
		self.ufile_image_entry = Entry(self.file_options_frame, width = 30, bg = self.inp_field_color, fg = self.entry_text_color, bd = "0px", 
			insertbackground = self.entry_text_color)
		self.ufile_image_entry.place(x = "10px", y = "30px")

		self.import_file_button = Button(self.file_options_frame, text = "Import", bg = self.btn_colot_dark, fg =self.text_color, width = 10, bd = "0px",
			command = lambda: self.importPicture(self.ufile_image_entry.get()))
		self.import_file_button.place(x = "10px", y = "60px")


		intro_text = Text(self.file_options_frame, bg = self.frame_dark_color, width = 70, height = 10, bd = "0px", fg = self.text_color,
			wrap = WORD)
		intro_text.place(x = "15px", y = "120px")

		text_file = open("text.txt", "r")
		message = text_file.read()
		intro_text.insert(END, message)
		intro_text.configure(state = "disabled", cursor = "arrow")

		preview_button = Button(self.file_options_frame, text = "Preview", bg = self.btn_colot_dark, fg =self.text_color, width = 10, bd = "0px", 
			command = lambda: previewImge(self.ufile_image_entry.get()))
		preview_button.place(x = "420px", y = "370px")


		def previewImge(image):
			try:
				image_file = get_pkg_data_filename(image)
				image_data = fits.getdata(image_file, ext=0)

				plt.figure()
				plt.imshow(image_data, cmap='gray')
				plt.colorbar()
				plt.show()
			except Exception as error:
				print(error)


	def importPicture(self, image_name):
		self.imported_image = image_name
		self.image_file = get_pkg_data_filename(self.imported_image)
		self.image_data = fits.getdata(self.image_file, ext=0)


	def inspectDataFrame(self):
		self.file_inspect_data_frame = Frame(self.main_window, bg = self.frame_dark_color, width = "500px", height = "400px")
		self.file_inspect_data_frame.place(x = "100px", y = "0px")

		self.output_shell = Text(self.file_inspect_data_frame, bg = self.frame_dark_color, fg = self.text_dark_color, width = 80, height = 15)
		self.output_shell.place(x = "7px", y = "10px")


	def showHistogram(self):
		NBINS = 1000
		histogram = plt.hist(self.image_data.flatten(), NBINS)
		plt.show()




if __name__ == "__main__":
	run = Main()
	run.MainFrameWidgets()