# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideMenstruationInfo(Action):

    def name(self) -> str:
        return "action_provide_menstruation_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        menstruation_info = (
            "Menstruation is the monthly shedding of the uterine lining. It can affect mood and physical health. "
            "For more details, refer to [PubMed](https://pubmed.ncbi.nlm.nih.gov/). Common symptoms include cramps, "
            "bloating, and mood swings. Managing menstrual pain can include over-the-counter pain relief, exercise, "
            "and relaxation techniques. A balanced diet and hydration can also help."
        )
        dispatcher.utter_message(text=menstruation_info)
        return []

class ActionProvideMenopauseInfo(Action):

    def name(self) -> str:
        return "action_provide_menopause_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        menopause_info = (
            "Menopause marks the end of a woman's reproductive years. Symptoms can include hot flashes, night sweats, "
            "mood changes, and sleep problems. Learn more at [JAMA](https://jamanetwork.com/). Treatments range from "
            "hormone replacement therapy to natural remedies like dietary changes and exercise. Consult with a healthcare "
            "provider for personalized advice."
        )
        dispatcher.utter_message(text=menopause_info)
        return []

class ActionProvideHormonalCyclesInfo(Action):

    def name(self) -> str:
        return "action_provide_hormonal_cycles_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        hormonal_cycles_info = (
            "Hormonal cycles include phases like menstruation, follicular phase, ovulation, and luteal phase. These cycles "
            "impact both physical and mental health. For in-depth information, visit [The Lancet](https://www.thelancet.com/). "
            "Hormonal fluctuations can affect mood, energy levels, and physical symptoms like acne. Understanding your cycle "
            "can help manage these effects."
        )
        dispatcher.utter_message(text=hormonal_cycles_info)
        return []

class ActionProvidePsychologicalImpactsInfo(Action):

    def name(self) -> str:
        return "action_provide_psychological_impacts_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        psychological_impacts_info = (
            "Hormonal changes can significantly impact mental health, leading to mood swings, anxiety, and depression. "
            "Check out articles on [BMJ](https://www.bmj.com/). Coping strategies include therapy, medication, lifestyle changes, "
            "and support from friends and family. Regular exercise, a healthy diet, and mindfulness practices can also be beneficial."
        )
        dispatcher.utter_message(text=psychological_impacts_info)
        return []

class ActionProvideGuidelinesInfo(Action):

    def name(self) -> str:
        return "action_provide_guidelines_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        guidelines_info = (
            "Guidelines on managing women's health issues can be found at [NHS](https://www.nhs.uk/), [CDC](https://www.cdc.gov/), "
            "and [WHO](https://www.who.int/). It's important to follow best practices for menstrual hygiene, regular check-ups, and "
            "a healthy lifestyle. Specific guidelines for managing menopause and PMS are also available."
        )
        dispatcher.utter_message(text=guidelines_info)
        return []

class ActionProvideSupportInfo(Action):

    def name(self) -> str:
        return "action_provide_support_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        support_info = (
            "I'm here to provide emotional support. It's important to talk about how you're feeling. Please share more about what's going on. "
            "You can also find support groups, online communities, and hotlines for immediate help. Mindfulness, relaxation techniques, "
            "and self-care practices can help manage stress and anxiety."
        )
        dispatcher.utter_message(text=support_info)
        return []

class ActionProvideResourcesInfo(Action):

    def name(self) -> str:
        return "action_provide_resources_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        resources_info = (
            "You can find more information on women's health at [PubMed](https://pubmed.ncbi.nlm.nih.gov/), [Mayo Clinic](https://www.mayoclinic.org/), "
            "and [Johns Hopkins Medicine](https://www.hopkinsmedicine.org/). Support groups, books, podcasts, and reputable blogs are also valuable resources. "
            "Online courses and documentaries can provide in-depth knowledge."
        )
        dispatcher.utter_message(text=resources_info)
        return []

class ActionProvideVenusAppInfo(Action):

    def name(self) -> str:
        return "action_provide_venus_app_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        venus_app_info = (
            "The Venus app offers features to track your menstrual cycle, manage menopause symptoms, and provide mental health support. "
            "It includes personalized advice, health tips, and resources for women's health. The app can send medication reminders, sync with fitness trackers, "
            "and offers a community feature for support."
        )
        dispatcher.utter_message(text=venus_app_info)
        return []
