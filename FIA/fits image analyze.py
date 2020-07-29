from tkinter import *
import matplotlib.pyplot as plt 
from astropy.io import fits
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
import numpy as np 




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

		self.information_frame = Button(self.side_options_frame, text = "information", width = 16, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: frameToggles("inspect data"))
		self.information_frame.place_forget()

		self.fileOptionsFrame()

		
		def frameToggles(frame_name):
			if frame_name == "file options":
				self.fileOptionsFrame()
				self.information_frame.place_forget()

			elif frame_name == "inspect data":
				self.information()
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
				plt.style_use(astropy_mpl_style)
				image_file = get_pkg_data_filename(image)
				image_data = fits.getdata(image_file, ext=0)

				plt.figure()
				plt.imshow(image_data, cmap='gray')
				plt.colorbar()
				plt.show()
			except Exception as error:
				print(error)


	def importPicture(self, image_name):
		try:
			self.imported_image = image_name
			self.image_file = get_pkg_data_filename(self.imported_image)
			self.image_data = fits.getdata(self.image_file, ext=0)

			self.information_frame.place(x = "4px", y = "30px")
		except Exception as error:
			print(error)


	def information(self):

		self.information_frame = Frame(self.main_window, bg = self.frame_dark_color, width = "500px", height = "400px")
		self.information_frame.place(x = "100px", y = "0px")

		self.image_size_information = Frame(self.information_frame, bg = self.frame_dark_color, width = "100px", height = "100px", 
			highlightbackground = "black", highlightcolor="black", highlightthickness=1)
		self.image_size_information.place(x = "5px", y = "5px")
		Label(self.information_frame, text = "image information", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "0px")


		self.data_min = np.min(self.image_data)
		self.data_max = np.max(self.image_data)
		self.data_mean = np.mean(self.image_data)
		self.data_Stdev = np.std(self.image_data)


		Label(self.information_frame, text = "min:", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "20px")
		data_min = Entry(self.information_frame, fg = self.text_color, bg = self.frame_dark_color, width = 10, bd = "0px")
		data_min.insert(END, self.data_min)
		data_min.place(x = "50px", y = "20px")

		Label(self.information_frame, text = "max:", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "40px")
		data_max = Entry(self.information_frame, fg = self.text_color, bg = self.frame_dark_color, width = 10, bd = "0px")
		data_max.insert(END, self.data_max)
		data_max.place(x = "50px", y = "40px")

		Label(self.information_frame, text = "mean:", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "60px")
		data_mean = Entry(self.information_frame, fg = self.text_color, bg = self.frame_dark_color, width = 10, bd = "0px")
		data_mean.insert(END, self.data_mean)
		data_mean.place(x = "50px", y = "60px")

		Label(self.information_frame, text = "Stdev:", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "80px")
		data_Stdev = Entry(self.information_frame, fg = self.text_color, bg = self.frame_dark_color, width = 10, bd = "0px")
		data_Stdev.insert(END, self.data_Stdev)
		data_Stdev.place(x = "50px", y = "80px")


		self.show_info = Button(self.information_frame, text = "image statistics", width = 16, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: printImageInfo())
		self.show_info.place(x = "5px", y = "120px")

		view_image = Button(self.information_frame, text = "view image", bg = self.btn_colot_dark, fg =self.text_color, width = 10, bd = "0px", 
			command = lambda: self.viewImage())
		view_image.place(x = "420px", y = "370px")

		view_histogram = Button(self.information_frame, text = "view histogram", bg = self.btn_colot_dark, fg =self.text_color, width = 10, bd = "0px", 
			command = lambda: self.showHistogram())
		view_histogram.place(x = "360px", y = "370px")

		def printImageInfo():
			self.info = fits.info(self.image_file)



	def viewImage(self):
		plt.style_use(astropy_mpl_style)
		plt.figure()
		plt.imshow(self.image_data)
		plt.colorbar()
		plt.show()


	def showHistogram(self):
		plt.style.use("ggplot")
		NBINS = 1000
		histogram = plt.hist(self.image_data.flatten(), NBINS)
		plt.show()



if __name__ == "__main__":
	run = Main()
	run.MainFrameWidgets()