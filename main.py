from functions.greet_and_speak import greet_user, take_user_input, speak
from functions.os_ops import *
from functions.online_ops import *
from functions.side_fucntions import match_prompt

if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input().lower()
        prompt = match_prompt(query)

        match prompt:
            
            # Offline operations
            case 'open notepad':
                open_notepad()
            case 'open discord':
                open_discord()
            case 'open command prompt':
                open_cmd()
            case 'open camera':
                open_camera()
            case 'open calculator':
                open_calculator()

            # Online operations
            case 'search on google':
                speak('What do you want to search on Google?')
                query = take_user_input().lower()
                search_on_google(query)
            case 'news':
                speak(f'I\'m reading out the latest news sir')
                speak(get_latest_news())
                speak('For your convenience I am printing it on screen sir.')
                print(*get_latest_news(), sep = '\n')
            case 'weather':
                ip_address = find_my_ip()
                city = requests.get(f'https://ipapi.co/{ip_address}/city/').text
                speak(f'Getting weather report for your city {city}')
                weather, temperature, feels_like = get_weather_report(city)
                speak(f'The current temperature is {temperature}, but feels like {feels_like}')
                speak(f'Also, the weather report talks about {weather}')
                speak(f'For your convenience, I am printing it on screen, sir')
                print(f'Description: {weather}\nTemperature: {temperature}\nFeels Like: {feels_like}')