# Vision Automation
### Computer vision package focused on automation and RPA

A different way of using PyAutoGui. Focused on automations where we can have page bars with captchas and reCaptchas that prevent us from using the Selenium Driver, for example. In this package, there is a way of using PyAutoGui the name of images saved in a template folder, making the code search the page and execute what you want. 

It works in a simple way: When you pass an image, the code will compare the main screen with the image passed, with 80% assertiveness by default (in some cases this value has to be reduced, when searching for tokens and values that maintain formatting but change frequently, for example). If the image is found on the screen, it proceeds to take the desired action, be it a double or single click, or even selecting a captcha checkbox.

#### How to use it?

> [!NOTE]  
> Python version used for testing: **3.11.9**
> 
> Dependencies: `pip install -r requirements.txt`

In this example I'm using a template folder literally called "templates".

First we need to initialize the VisionAutomation class.

```py
import os
from src.vision import VisionAutomation 

parent_directory = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(parent_directory, 'templates') # Getting the folder path 

vision = VisionAutomation(template_path)
```

From now on you can take the names of the images saved in your templates folder and use them as parameters for VisionAutomation's methods. For example:

A click of a button:
```py
vision.click("buton.png")
```

Click and write on an input:
```py
vision.click_write("input_simple.png", "Value to be written to the input")
```

A token that needs to be copied and pasted elsewhere.
It's important to remember that the confidence in this case is 50% (0.5) because the token keeps the same formatting, but its value always changes. For example, it will always be red block letters, but they are different letters.
```py
vision.double_click_and_copy("token.png", confidence=0.5)
```

In short, there is a huge range of combinations of functions that can exist and various scenarios where they can be applied. 
But thank you for visiting and taking an interest in the VisionAutomation project. I'm always available and I hope this project helps you or inspires you in some way. 

```py
print("Thank you very much ❤️")
```
