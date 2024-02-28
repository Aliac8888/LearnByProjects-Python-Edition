# Program to take screenshot 
import pyscreenshot
  
# To capture the screen 
image = pyscreenshot.grab() 
  
# To display the captured screenshot 
image.show() 
  
name_of_pic = input("enter a name for the screenshot to be saved : ")

# To save the screenshot 
image.save(f"beginner_projects/pyscreenshot_project/{name_of_pic}.png")