from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, JavascriptException

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
xp = By.XPATH 

with open('paths.json', 'r') as f:
    paths = json.load(f)



def get_name():
    try:
        return driver.find_element(xp, paths['name_path']).get_attribute('innerText')
    except Exception as e:
        print(f"Error fetching name: {e}")
        return ""

def get_category():
    try:
        return driver.find_element(xp, paths['cat_path']).get_attribute('innerText')
    except Exception as e:
        print(f"Error fetching category: {e}")
        return ""

def get_types():
    try:
        elements = driver.find_elements(xp, paths['types_path'])
        return [type.get_attribute('innerText') for type in elements]
    except Exception as e:
        print(f"Error fetching types: {e}")
        return []

def get_abilities():
    try:
        elements = driver.find_elements(xp, paths['abilities_path'])
        return [ab.get_attribute('innerText') for ab in elements]
    except Exception as e:
        print(f"Error fetching abilities: {e}")
        return []

def get_gender_ratios():
    try:
        elements = driver.find_elements(xp, paths['gender_ratio_path'])
        ratios = [gr.get_attribute('innerText') for gr in elements]
        if ratios != []:
            male_ratio = ratios[0]
            female_ratio = ratios[1]
            return male_ratio, female_ratio
        else:
            male_ratio = female_ratio = 'Gender unknown'
            return male_ratio, female_ratio

    except Exception as e:
        print(f"Error fetching gender: {e}")
        

def get_catch_rate():
    try:
        return driver.find_element(xp, paths['catch_rate_path']).get_attribute('innerText')
    except Exception as e:
        print(f"Error fetching catch rate: {e}")
        return ""

def get_egg_groups():
    try:
        return driver.find_element(xp, paths['egg_group_path']).get_attribute('innerText')
            
    except NoSuchElementException:
        return driver.find_element(xp, paths['secondary_egg_group_path']).get_attribute('innerText')


def get_hatch_time():
    try:
        return driver.find_element(xp, paths['hatch_time_path']).get_attribute('innerText')

            
    except Exception as e:
            return driver.find_element(xp, paths['secondary_hatch_time_path']).get_attribute('innerText')

def get_height():
    try:
        return driver.find_element(xp, paths['height_path']).get_attribute('innerText')
    except Exception as e:
        print(f"Error fetching height: {e}")
        return ""

def get_weight():
    try:
        return  driver.find_element(xp, paths['weight_path']).get_attribute('innerText')
            
    except NoSuchElementException:
        return driver.find_element(xp, paths['secondary_weight_path']).get_attribute('innerText')

def get_exp_yield():
    try:
        return driver.find_element(xp, paths['exp_yield_path']).get_attribute('innerText')
    except Exception as e:
        print(f"Error fetching exp yield: {e}")
        return ""

def get_lvl_rate():
    try:
        return driver.find_element(xp, paths['levelling_rate_path']).get_attribute('innerText')
            
    except NoSuchElementException:
        return driver.find_element(xp, paths['secondary_levelling_rate_path']).get_attribute('innerText')

def get_evs():
    try:
        elements = driver.find_elements(xp, paths['evs_path'])
        return [ev.get_attribute('innerText') for ev in elements]
    except Exception as e:
        print(f"Error fetching EVs: {e}")
        return []

def get_base_friendship():
    try:
        return driver.find_element(xp, paths['friendship_path']).get_attribute('innerText')
            
    except Exception as e:
        return driver.find_element(xp, paths['secondary_friendship_path']).get_attribute('innerText')

def get_evolution():
    try:
        return driver.find_element(xp, paths['evo_info_path']).get_attribute('innerText')
    except Exception as e:
        print(f"Error fetching evolution info: {e}")
        return ""

def get_locations(clean_locs):
    try:
        locs = driver.find_elements(xp, paths['locations_path'])[1]
        locs = locs.find_elements(xp, "./tbody//tr//td[contains(@class, 'roundy')]")
        return clean_locs(locs)
    except Exception as e:
        print(f"Error fetching locations: {e}")
        return []

def get_stats():
    try:
        elements = driver.find_elements(xp, paths['stats_path'])
        return [stat.get_attribute('innerText') for stat in elements]
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return []

def get_type_effectiveness():
    try:
        elements = driver.find_elements(xp, paths['type_effectivness_path'])
        return [eff.get_attribute('innerText') for eff in elements]
    except Exception as e:
        print(f"Error fetching type effectiveness: {e}")
        return []

def get_moves():
    try:
        moves = driver.find_element(xp, paths['moves_path'])
        moves = moves.find_elements(xp, ".//tr")
        return [move.get_attribute('innerText') for move in moves]
    except NoSuchElementException:
        return "No moves in gen 9"
        
def get_generation():
    try:
        return driver.find_element(xp, paths['generation_path']).get_attribute('innerText')
    except Exception as e:
        print(f"Error fetchin generation: {e}")
        return ""

def clean_locs(locs):
        locations = []
        
        for loc in locs:
                loc = loc.get_attribute('innerText')
                if loc not in locations:
                        locations.append(loc)
    

        cleaned_locations = []
        for i in range(len(locations)):
                is_substring = False
                for j in range(len(locations)):
                        if i != j and locations[i] in locations[j]:
                                is_substring = True
                                break
                if not is_substring:
                        cleaned_locations.append(locations[i])
        
        return cleaned_locations

