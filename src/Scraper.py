from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, JavascriptException
import pandas as pd
from utils import *


url = 'https://bulbapedia.bulbagarden.net/wiki/Mewtwo_(Pok%C3%A9mon)'
driver.get(url) #imported from utils





def get_data(driver):
        name = get_name()
        category = get_category()
        generation = get_generation()
        types = get_types()
        abilities = get_abilities()
        male_ratio, female_ratio = get_gender_ratios()
        catch_rate = get_catch_rate()
        egg_groups = get_egg_groups()
        hatch_time = get_hatch_time()
        height = get_height()
        weight = get_weight()
        exp_yield = get_exp_yield()
        lvl_rate = get_lvl_rate()
        evs = get_evs()
        base_friendship = get_base_friendship()
        evolution = get_evolution()
        locs = get_locations(clean_locs)
        stats = get_stats()
        type_effectiveness = get_type_effectiveness()
        moves = get_moves()

        if type(moves) == list:
                moves = '???'.join(moves)



        pokemon_info = {
        "Name": name,
        "Category": category,
        "Generation": generation,
        "Types": ' '.join(types),
        "Abilities": ' '.join(abilities),
        "Catch_Rate": catch_rate,
        "Egg_Groups": egg_groups,
        "Hatch_Time": hatch_time,
        "Height": height,
        "Weight": weight,
        "Exp_Yield": exp_yield,
        "Level_Rate": lvl_rate,
        "Evs": ' '.join(evs),
        "Base_Friendship": base_friendship,
        "Evolution_info": evolution,
        "Male_Ratio": male_ratio,
        "Female_Ratio": female_ratio,
        "Locations": '???'.join(locs),
        "Stats": '???'.join([str(stat) for stat in stats]),
        "Type_effectiveness": ' '.join(type_effectiveness),
        "Moves": moves
        }

        return pokemon_info


def print_pokemon(data):
        print(data["Name"])



def privacy_check_accept(driver):           
        try:
                shadow_host = driver.find_element(By.CSS_SELECTOR, '#cmpwrapper')
        
        except NoSuchElementException:
                try:
                        shadow_host = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cmpwrapper')))
                except TimeoutException as e:
                        print(f"Timeout waiting for shadow host: {e}")
                        shadow_host = None

        if shadow_host:
                try:
                        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
                        
                        element = shadow_root.find_element(By.CSS_SELECTOR, '#cmpwelcomebtnyes > a')
                        element.click()

                except (JavascriptException, NoSuchElementException, TimeoutException) as e:
                        print(f"Error interacting with shadow DOM: {e}")
        else:
                print("Shadow host element was not found.")


def goto_next_page(driver):
        try:
                next_arrow = driver.find_element(xp, "//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[2]/td[3]/table/tbody/tr/td[3]/a")
                next_arrow.click()
        except NoSuchElementException:
                print("Error locating to next page")


if __name__ == "__main__":
        
        data = []
        privacy_check_accept(driver)
        data.append(get_data(driver))
        print(1)
        for i in range(1):
                goto_next_page(driver)
                data.append(get_data(driver))
                print(i+2)


        df = pd.DataFrame(data)
        df.to_csv('pokemony.csv')

        driver.quit()




        
