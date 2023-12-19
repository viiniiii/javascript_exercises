import tkinter as tk

from tkinter import filedialog

from PIL import Image, ImageTk, ImageDraw, ImageFont



class WatermarkApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Image Watermark App")



        self.canvas = tk.Canvas(self.root, width=400, height=400)

        self.canvas.pack()



        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)

        self.upload_button.pack()



        self.watermark_button = tk.Button(self.root, text="Add Watermark", command=self.add_watermark)

        self.watermark_button.pack()



        self.image_path = None

        self.image = None

        self.watermark_text = "Watermark"

        self.watermark_position = (10, 10)



    def upload_image(self):

        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])

        if self.image_path:

            self.image = Image.open(self.image_path)

            self.image.thumbnail((400, 400))

            self.photo = ImageTk.PhotoImage(self.image)

            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)



    def add_watermark(self):

        if self.image_path and self.image:

            image_with_watermark = self.image.copy()

            draw = ImageDraw.Draw(image_with_watermark)

            font = ImageFont.load_default()  # You can use a different font if desired

            draw.text(self.watermark_position, self.watermark_text, fill=(255, 255, 255), font=font)

            image_with_watermark.show()



def main():

    root = tk.Tk()

    app = WatermarkApp(root)

    root.mainloop()



if __name__ == "__main__":

    main()
