from tkinter import *
import matplotlib.pyplot as plt 
from astropy.io import fits
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
import numpy as np 
from PIL import Image


class Main():

	def __init__(self):
		self.root = Tk()
		self.root.title("FIA")
		self.root.wm_iconbitmap('icon.ico')

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


		self.file_options_button = Button(self.side_options_frame, text = "file options", width = 16, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: frameToggles("file options"))
		self.file_options_button.place(x = "4px", y = "10px")

		self.information_button = Button(self.side_options_frame, text = "information", width = 16, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: frameToggles("inspect data"))
		self.information_button.place_forget()

		self.header_button = Button(self.side_options_frame, text = "Header", width = 16, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: frameToggles("header option"))
		self.header_button.place_forget()


		self.fileOptionsFrame()
			
		
		def frameToggles(frame_name):
			print(frame_name)
			if frame_name == "file options":
				self.fileOptionsFrame()

			elif frame_name == "inspect data":
				self.information_frame.place(x = "100px", y = "0px")
				self.header_frame.place_forget()
				self.file_options_frame.place_forget()

			elif frame_name == "header option":
				self.header_frame.place(x = "100px", y = "0px")
				self.information_frame.place_forget()
				self.file_options_frame.place_forget()

		self.root.resizable(0,0)
		self.root.mainloop()



	def fileOptionsFrame(self):
		self.file_options_frame = Frame(self.main_window, bg = self.frame_dark_color, width = "500px", height = "400px")
		self.file_options_frame.place(x = "100px", y = "0px")

		Label(self.file_options_frame, text = "import .fits", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "10px")
		self.ufile_image_entry = Entry(self.file_options_frame, width = 30, bg = self.inp_field_color, fg = self.entry_text_color, bd = "0px", 
			insertbackground = self.entry_text_color)
		self.ufile_image_entry.place(x = "10px", y = "30px")

		self.import_file_button = Button(self.file_options_frame, text = "Import", bg = self.btn_colot_dark, fg =self.text_color, width = 10, bd = "0px",
			command = lambda: self.importPicture(self.ufile_image_entry.get()))
		self.import_file_button.place(x = "10px", y = "60px")

		preview_button = Button(self.file_options_frame, text = "Preview", bg = self.btn_colot_dark, fg =self.text_color, width = 10, bd = "0px", 
			command = lambda: previewImge(self.ufile_image_entry.get()))
		preview_button.place(x = "70px", y = "60px")




		Label(self.file_options_frame, text = "import .jpg", bg = self.frame_dark_color, fg = self.text_color).place(x = "310px", y = "10px")
		self.ufile_jpg_image_entry = Entry(self.file_options_frame, width = 30, bg = self.inp_field_color, fg = self.entry_text_color, bd = "0px", 
			insertbackground = self.entry_text_color)
		self.ufile_jpg_image_entry.place(x = "310px", y = "30px")

		self.seperate_jpg_file_button = Button(self.file_options_frame, text = "Seperate", bg = self.btn_colot_dark, fg =self.text_color, width = 10, bd = "0px",
			command = lambda: self.seperateRGBImage(self.ufile_jpg_image_entry.get()))
		self.seperate_jpg_file_button.place(x = "310px", y = "60px")

		self.view_jpg_file_button = Button(self.file_options_frame, text = "preview", bg = self.btn_colot_dark, fg =self.text_color, width = 10, bd = "0px",
			command = lambda: self.previewRGBimage(self.ufile_jpg_image_entry.get()))
		self.view_jpg_file_button.place(x = "370px", y = "60px")





		intro_text = Text(self.file_options_frame, bg = self.frame_dark_color, width = 70, height = 20, bd = "0px", fg = self.text_color,
			wrap = WORD)
		intro_text.place(x = "15px", y = "160px")

		text_file = open("text.txt", "r")
		message = text_file.read()
		intro_text.insert(END, message)
		intro_text.configure(state = "disabled", cursor = "arrow")



		


		def previewImge(image):
			try:
				plt.style.use(astropy_mpl_style)
				image_file = get_pkg_data_filename(image)
				image_data = fits.getdata(image_file, ext=0)

				plt.figure()
				plt.imshow(image_data, cmap='gray')
				plt.colorbar()
				plt.show()
			except Exception as error:
				print(error)



	def importPicture(self, image_name):
		def initializeFrames():
			self.fileOptionsFrame()

			print("called")

			self.information()
			self.information_frame.place_forget()
			print("called")

			self.header()
			self.header_frame.place_forget()
			print("called")


		try:
			self.imported_image = image_name
			self.image_file = get_pkg_data_filename(self.imported_image)
			self.image_data = fits.getdata(self.image_file, ext=0)

			self.information_button.place(x = "4px", y = "30px")
			self.header_button.place(x = "4px", y = "50px")

			initializeFrames()

		except Exception as error:
			print(error)



	def information(self):
		self.information_frame = Frame(self.main_window, bg = self.frame_dark_color, width = "500px", height = "400px")
		self.information_frame.place(x = "100px", y = "0px")

		self.image_size_information = Frame(self.information_frame, bg = self.frame_dark_color, width = "100px", height = "100px", 
			highlightbackground = "black", highlightcolor="black", highlightthickness=1)
		self.image_size_information.place(x = "5px", y = "5px")
		Label(self.information_frame, text = "Statistics", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "0px")


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


		Label(self.information_frame, text = "color filter:", bg = self.frame_dark_color, fg = self.text_color).place(x = "390px", y = "5px")
		self.image_cmap = StringVar(self.information_frame)
		self.image_cmap.set("BrBG")

		cmap_options = OptionMenu(self.information_frame, self.image_cmap, 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 
			'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 
			'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 
			'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 
			'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 
			'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 
			'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 
			'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 
			'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 
			'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 
			'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 
			'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 
			'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 
			'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r')
		cmap_options.place(x = "390px", y = "20px")
		cmap_options.config(width = 15, bg = self.btn_colot_dark, fg = self.text_color, bd = "0px", highlightbackground = "black", 
		highlightcolor="black", highlightthickness=1)




		self.show_info = Button(self.information_frame, text = "image information", width = 15, bg = self.btn_colot_dark, bd = "0px", fg =  "white",
			command = lambda: printImageInfo())
		self.show_info.place(x = "220px", y = "370px")


		view_histogram = Button(self.information_frame, text = "view histogram", bg = self.btn_colot_dark, fg =self.text_color, width = 15, bd = "0px", 
			command = lambda: self.showHistogram())
		view_histogram.place(x = "310px", y = "370px")


		view_image = Button(self.information_frame, text = "view image", bg = self.btn_colot_dark, fg =self.text_color, width = 15, bd = "0px", 
			command = lambda: self.viewImage(self.image_cmap.get()))
		view_image.place(x = "400px", y = "370px")
		

		def printImageInfo():
			self.info = fits.info(self.image_file)


	def header(self):
		self.header_frame = Frame(self.main_window, bg = self.frame_dark_color, width = "500px", height = "400px")
		self.header_frame.place(x = "100px", y = "0px")

		self.header_output_screen = Text(self.header_frame, bg = self.frame_dark_color, fg = self.text_color, width = 80, height = 7, wrap = WORD)
		self.header_output_screen.place(x = "7px", y = "2px")

		expand_header = Button(self.header_frame, text = "expand", bg = self.btn_colot_dark, fg =self.text_color, width = 15, bd = "0px", 
			command = lambda: expandHeader())
		expand_header.place(x = "400px", y = "90px")


		Label(self.header_frame, text = "show header", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "100px")
		self.uinp_header = Entry(self.header_frame, bg = self.frame_dark_color, width = 10)
		self.uinp_header.place(x = "10px", y = "120px")

		view_header = Button(self.header_frame, text = "execute", bg = self.btn_colot_dark, fg =self.text_color, width = 15, bd = "0px", 
			command = lambda: getHeader())
		view_header.place(x = "70px", y = "120px")


		Label(self.header_frame, text = "change value of:", bg = self.frame_dark_color, fg = self.text_color).place(x = "10px", y = "160px")
		self.uinp_change_header_value = Entry(self.header_frame, bg = self.frame_dark_color, width = 15)
		self.uinp_change_header_value.place(x = "10px", y = "180px")

		Label(self.header_frame, text = "value:", bg = self.frame_dark_color, fg = self.text_color).place(x = "120px", y = "160px")
		self.uinp_change_header_new_value = Entry(self.header_frame, bg = self.frame_dark_color, width = 15)
		self.uinp_change_header_new_value.place(x = "100px", y = "180px")

		change_header_value = Button(self.header_frame, text = "execute", bg = self.btn_colot_dark, fg =self.text_color, width = 15, bd = "0px", 
			command = lambda: changeHeaderValue(self.uinp_change_header_value.get(), self.uinp_change_header_new_value.get()))
		change_header_value.place(x = "10px", y = "200px")


		def changeHeaderValue(key_name, new_val):
			try:
				fits.setval(self.image_file, key_name, value = new_val)
				getHeader()
			except Exception as error:
				print("--!--" + str(error) + "--!--")


		def getHeader():
			try:
				self.header_output = (repr(fits.getheader(self.image_file, int(self.uinp_header.get()))))
				self.header_output_screen.delete(END, "1.0")
				self.header_output_screen.insert(END, str(self.header_output))
				self.header_output_screen.configure(state = "disabled", cursor = "arrow")

			except IndexError:
				print("--!-- header input out of index --!--")

			except ValueError:
				print("--!-- invalid header input --!--")

		def expandHeader():
			header_window = Tk()
			header_window.title("header")

			header_expanded_screen = Text(header_window, bg = self.frame_dark_color, fg = self.text_color, width = 120, height = 40, wrap = WORD)
			header_expanded_screen.pack()

			try:
				header_expanded_screen.insert(END, str(self.header_output))
			except AttributeError:
				print("--!-- no inputs --!--")

			header_expanded_screen.configure(state = "disabled", cursor = "arrow")

			header_window.resizable(0,0)
			header_window.mainloop()


	def previewRGBimage(self, unip_RGB_image):
		try:
			rgb_image = Image.open(unip_RGB_image)
			xsize, ysize = rgb_image.size
			print("RGB Image size: {} x {}".format(xsize, ysize))
			plt.figure(figsize = (5,3)).patch.set_facecolor(self.frame_dark_color)
			plt.rc_context({'axes.edgecolor':'black', 'xtick.color':'white', 'ytick.color':'white', 'figure.facecolor':'white'})
			plt.imshow(rgb_image)
			plt.show()

		except Exception as error:
			print("--!--" + str(error) + "--!--")


	def seperateRGBImage(self, unip_RGB_image):
		try:
			rgb_image = Image.open(unip_RGB_image)
			xsize, ysize = rgb_image.size

			r, g, b = rgb_image.split()
			r_data = np.array(r.getdata())
			g_data = np.array(g.getdata())
			b_data = np.array(b.getdata())

			r_data = r_data.reshape(ysize, xsize)
			g_data = g_data.reshape(ysize, xsize)
			b_data = b_data.reshape(ysize, xsize)

			red = fits.PrimaryHDU(data=r_data)
			red.header['LATOBS'] = "32:11:56"
			red.header['LONGOBS'] = "110:56"
			red.writeto('FIA_red.fits')

			green = fits.PrimaryHDU(data=g_data)
			green.header['LATOBS'] = "32:11:56"
			green.header['LONGOBS'] = "110:56"
			green.writeto('FIA_green.fits')

			blue = fits.PrimaryHDU(data=b_data)
			blue.header['LATOBS'] = "32:11:56"
			blue.header['LONGOBS'] = "110:56"
			blue.writeto('FIA_blue.fits')

			print(">>> jpg seperated succesfully (stored in folder where program is started)")

		except Exception as error:
			print("--!--" + str(error) + "--!--")



	def viewImage(self, cmap_value):
		try:
			plt.style.use(astropy_mpl_style)
			plt.figure(figsize = (7, 5)).patch.set_facecolor(self.frame_dark_color)
			plt.rc_context({'axes.edgecolor':'black', 'xtick.color':'white', 'ytick.color':'white', 'figure.facecolor':'white'})
			plt.imshow(self.image_data, cmap = cmap_value)
			plt.colorbar()
			plt.show()

		except Exception as error:
			print("--!--" + str(error) + "--!--")

		

	def showHistogram(self):
		try:
			plt.figure(figsize = (5,3)).patch.set_facecolor(self.frame_dark_color)
			
			plt.style.use("ggplot")
			plt.rc_context({'axes.edgecolor':'black', 'xtick.color':'white', 'ytick.color':'white', 'figure.facecolor':'white'})

			plt.rcParams["axes.facecolor"] = "#bdbdbd"

			NBINS = 1000
			histogram = plt.hist(self.image_data.flatten(), NBINS)
			plt.show()

		except Exception as error:
			print("--!--" + str(error) + "--!--")


if __name__ == "__main__":
	run = Main()
	run.MainFrameWidgets()