import pyautogui
from time import sleep

class VisionAutomation:
    def __init__(self, template_path: str):
        """
        Initialize the Vision class.

        Args:
            template_path (str): Place where template images for automation will be stored.
        """        
        self.template_path = template_path


    def find_element(self, template_name: str, confidence: float = 0.8) -> tuple[int, int]:
        """
        Find an element on the screen using a template image.

        Args:
            template_name (str): The name of the template image file.
            confidence (float): The confidence threshold (default is 0.8).

        Returns:
            tuple[int, int]: The (x, y) coordinates of the center of the found element.

        Raises:
            Exception: If the element is not found on the screen.
        """
        element = pyautogui.locateCenterOnScreen(f"{self.template_path}/{template_name}", confidence=confidence)
        
        if element is not None:
            return element
        else:
            raise Exception(f"Element {template_name} not found on the screen.")


    def is_element_present(self, element: str, confidence: float = 0.8)-> bool:
        """
        Check if a specific element is present on the screen. If yes, return True, otherwise False.
        Similar to find_element, but without returning an exception.

        Args:
            vision (VisionAutomation): The VisionAutomation instance.
            element (str): The name of the element image file.
            confidence (float): The confidence threshold (default is 0.8).

        Returns:
            bool: Returns True if the element is found on the screen, otherwise False
        """    
        try:
            self.find_element(element, confidence)
            return True
        
        except Exception:
            return False


    def click(self, template_name: str, confidence: float = 0.8):
        """
        Perform a mouse click on an element found using a template image.

        Args:
            template_name (str): The name of the template image file.
            confidence (float): The confidence threshold (default is 0.8).
        """
        try:
            x, y = self.find_element(template_name, confidence)
            pyautogui.click(x, y)
        except Exception as e:
            raise Exception(f"click() - Error: {e}")


    def paste(self, template_name: str, confidence: float = 0.8):
        """
        Paste text into an input field found using a template image.

        Args:
            template_name (str): The name of the template image file.
            confidence (float): The confidence threshold (default is 0.8).
        """
        try:
            x, y = self.find_element(template_name, confidence)
            pyautogui.click(x, y)
            pyautogui.hotkey('ctrl', 'v')
        except Exception as e:
            raise Exception(f"paste() - Error: {e}")


    def double_click_and_copy(self, template_name: str, confidence: float = 0.8):
        """
        Double clicks on an element identified by the given template name and copies the selected content.

        Args:
            template_name (str): _description_
            confidence (float, optional): _description_ (default is 0.8).
        """        
        try: 
            x, y = self.find_element(template_name, confidence)
            pyautogui.doubleClick(x, y)
            pyautogui.hotkey('ctrl', 'c')
        
        except Exception as e:
            raise Exception(f"double_click_and_copy() - Error: {e}")
        

    def select_and_copy(self, template_name_start: str, template_name_end: str, confidence: float = 0.8):
        """
        Select and copy text from the screen using template images for start and end positions.

        Args:
            template_name_start (str): The name of the template image file for the start position.
            template_name_end (str): The name of the template image file for the end position.
            confidence (float): The confidence threshold (default is 0.8).
        """
        try:
            start_x, start_y = self.find_element(template_name_start, confidence)
            end_x, end_y = self.find_element(template_name_end, confidence)
            pyautogui.moveTo(start_x, start_y)
            pyautogui.dragTo(end_x, end_y, duration=0.5, button='left')
            pyautogui.hotkey('ctrl', 'c')
            
        except Exception as e:
            raise Exception(f"select_and_copy() - Error: {e}")


    def wait_for_element(self, template_name: str, confidence: float = 0.8, timeout: int = 60):
        """
        Wait for an element to appear on the screen within a specified timeout period.

        Args:
            template_name (str): The name of the template image file.
            confidence (float): The confidence threshold (default is 0.8).
            timeout (int): The maximum time to wait for the element to appear, in seconds (default is 30).

        Raises:
            TimeoutError: If the element does not appear within the timeout period.
        """
        elapsed_time = 0
        while elapsed_time < timeout:
            try:
                element = self.find_element(template_name, confidence)
                return element
            
            except Exception:
                sleep(1)
                elapsed_time += 1
                
        raise TimeoutError(f"Element {template_name} did not appear on the screen within {timeout} seconds.")
    

    def find_and_click_in_template(self, large_template_name: str, small_template_name: str, confidence: float = 0.8):
        """
        Find a smaller template image within a larger template image and click on it.

        Args:
            large_template_name (str): The name of the larger template image file.
            small_template_name (str): The name of the smaller template image file to find within the larger template.
            confidence (float): The confidence threshold for finding the smaller template (default is 0.8).

        Raises:
            Exception: If either the large or small template is not found, or if the small template is not found within the large template.
        """
        try:
            large_element = pyautogui.locateOnScreen(f"{self.template_path}/{large_template_name}", confidence=confidence)
            
            if large_element is None:
                raise Exception(f"Large template {large_template_name} not found on the screen.")

            region = (large_element.left, large_element.top, large_element.width, large_element.height)

            # Image search size restriction
            small_element = pyautogui.locateCenterOnScreen(f"{self.template_path}/{small_template_name}", region=region, confidence=confidence)

            if small_element is not None:
                pyautogui.moveTo(small_element)
                pyautogui.click()
                
            else:
                raise Exception(f"Small template {small_template_name} not found within large template {large_template_name}.")
        
        except Exception as e:
            raise Exception(f"find_and_click_in_template() - Error: {e}")