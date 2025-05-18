# This project is still in progress. For now, I'm focusing on making every object in the window dynamic.
# To achieve that, I'm keeping everything very simple at first so I can understand how everything works.
# Once I finish making everything dynamic, I'll start improving the visual design.
# After that, I plan to make it actually useful by adding the option to upload any image,
# and eventually turn it into a program that users can use daily on their operating system,
# simply by opening the app automatically when trying to view any image.


from tkinter import *
from PIL import ImageTk, Image

c=0

root = Tk()

def loading_image(image_source):
    global y_screen, x_screen, resized_x, img_ratio

    root.update_idletasks()
    x_screen = root.winfo_width()
    y_screen = root.winfo_height()

    #importando a imagem
    image_load = Image.open(f"images/{image_source}")

    #coletando a largura e altura da imagem d
    img_x, img_y = image_load.size

    #calculando a proporção da imagem
    img_ratio = img_x/img_y

    #altura da imagem de acordo com a altura da janela
    img_display_height = y_screen-500

    #definindo a nova largura com base na altura definida usando a proporção calculada
    resized_x = int(img_display_height*img_ratio)

    #criando a imagem redimensionada
    img_resized = image_load.resize((resized_x, img_display_height))

    #convertendo a imagem para poder usar no tkinter
    img_tk = ImageTk.PhotoImage(img_resized)

    return img_tk, resized_x



def window_resize(event):
    global img_ratio, images_path, c, img
    if event.widget == root:
        x_screen=event.width
        y_screen=event.height

        img, img_x = loading_image(images_path[c])
        imgLabel.config(image=img)
        new_width = img_x

        #Reposiciona sempre para manter o mesmo lugar
        delta = x_screen-new_width
        imgLabel.place(x=delta//2,y=y_screen//10)

        #reposiciona botao
        nextButton.place(x=(x_screen)//2 ,rely=0.9)
        backButton.place(x=(x_screen-105)//2,rely=0.9)
        exitButton.place(x=12/13*(x_screen),rely=0.9)

def change_image(direction):
    global c
    global images_path
    global img
    if direction == "next":
        if c < len(images_path)-1:
            c+=1
    elif direction == "back":
        if c > 0:
            c=c-1
    else:
        root.quit()
    img, nouse = loading_image(images_path[c])
    imgLabel.config(image=img)
    imgLabel.place(x=(x_screen-resized_x)//2,y=y_screen//10)
    print(c)       


#Tamanho Inicial da tela
x_screen = 1024
y_screen = 720

root.minsize(800,600)
root.geometry(f"{x_screen}x{y_screen}")

#interface basica
nextButton = Button(root, text=">>", padx=12,pady=5, command= lambda: change_image("next"))
backButton = Button(root, text="<<", padx=12,pady=5, command= lambda: change_image("back"))
exitButton = Button(root, text="Exit",padx=20,pady=5, command= lambda: change_image("exit"))

nextButton.place(x=(x_screen)//2 ,rely=0.9)
backButton.place(x=(x_screen-105)//2,rely=0.9)
exitButton.place(x=12/13*(x_screen),rely=0.9)

#Carregando a imagem    
images_path = ["mario1.png","carro.jpg","image1.png"]
img, nouse = loading_image("mario1.png")
imgLabel = Label(root, image=img)

imgLabel.place(x=(x_screen-resized_x)//2,y=y_screen//10)

#vincula o redimensionamento da tela
root.bind("<Configure>", window_resize)
root.mainloop()
