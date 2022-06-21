# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from asyncore import dispatcher
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionGetSymptom(Action):

    def name(self) -> Text:
        return "action_get_symptom"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        d = {
        'alveolar proteinosis': ['chest pain',
                                 'breathing difficulty',
                                 'alveolar inflammation',
                                 'alveolar lavage fluid visible',
                                 'fever with cough'],
        'pertussis': ['hanging sound when inhaling',
                      'chest tightness',
                      'twitching',
                      'low fever'],
        'asthmatic bronchitis': ['wheeling sound',
                                 'ciliated epithelial cell damage shedding',
                                 'allergic cough',
                                 'chemical bronchitis',
                                 'chronic cough',
                                 'cough with wheezing sound'],
        'adult respiratory distress syndrome': ['difficulty in breathing',
                                                'cough',
                                                'cardiac respiratory distress'],
        'large amount of amniotic fluid inhalation': ['face has bruises',
                                                      'lips are blue',
                                                      'lung texture thickening',
                                                      'lips and nail bed slightly blue-purple',
                                                      'out of breath'],
        'simple pulmonary eosinophilic infiltration': ['eosinophilia (increase in number of white blood cells)',
                                                       'tightning or choking feeling in pharynx',
                                                       'chest suffocation',
                                                       'lack of strength'],
        'lobular pneumonia': ['fever',
                              'cough rust color sputum',
                              'acute face',
                              'breathing sound weakened'],
        'pulmonary-pleural amebiasis': ['night sweat',
                                        'diarrhea',
                                        'lack of strength'],
        'pulmonary hemorrhage-nephritis syndrome': ['lung bleeding',
                                                    'short breath',
                                                    'hemoptysis',
                                                    'proteinuria (increased protein in urine)'],
        'lung actinomycosis': ['periostitis (inflammation of tissue around bone)',
                               'weight loss',
                               'night sweat',
                               'low fever'],
        'pulmonary aspergillosis': ['cough out brown sputum', 'eosinophilic'],
        'radiation pneumonitis': ['pulmonary fibrosis', 'low heat'],
        'lung bullae': ['short breath', 'chest suffocation', 'short breath'],
        'emphysema': ['industrial vertebrae expansion',
                      'barrel-thorax',
                      'small bronchial mucosal edema',
                      'sticky sputum',
                      'low diaphragm',
                      'exhalation sound',
                      'lung sounds'],
        'pneumonia': ['feeling chills', 'gas rush'],
        'lung abscess': ['development of a spot on lungs',
                         'lung pain',
                         'blood in my sputum',
                         'pus sputum'],
        'pulmonary embolism': ['right heart (right ventricle) failure',
                               'breathing difficulty',
                               'irregular heartbeat',
                               'large volume hemoptysis'],
        'lung bubble': ['short breath', 'chest suffocation'],
        'sars': ['chilling', 'sustained fever', 'lack of strength'],
        'lung metastases': ['thirsty vomiting', 'stationary doctor'],
        'pulmonary cryptococcosis': ['cryptococcus capsular polysaccharide accumulation',
                                     'sputum is mucopurulent',
                                     'low fever'],
        'lung cancer': ['cough',
                        'weight loss',
                        'hemoptysis with chest pain',
                        'lung nodules',
                        'stem in bloodshot'],
        'anaphylactic shock': ['pale lips',
                               'fainting/passing out',
                               'consciousness disorder',
                               'heart panic',
                               'hypotension'],
        'hypersensitivity pneumonitis': ['incapable',
                                         'allergic cough',
                                         'appetite loss',
                                         'lack of strength',
                                         'wheeze',
                                         'cough with wheezing sound'],
        'acute lung abscess': ['cough foam like sputum',
                               'rotten peach-like bloody sputum',
                               'sputum is mucopurus',
                               'sputum viscous or purulent',
                               'sputum is white viscous jelly',
                               'chills'],
        'legionnaires disease': ['shock',
                                 'respiratory failure',
                                 'muscle soreness',
                                 'muscle pain',
                                 'hair lice'],
        'legionellosis': ['diarrhea',
                          'sense is unclear',
                          'dizziness',
                          'less urine'],
        'tuberculous empyema': ['the gap between the ribs is narrowed',
                                'pleural effusion',
                                'hemoptysis',
                                'purulent sputum',
                                'cardiac tamponade'],
        'hemoptysis': ['lymph node enlargement',
                       'hemoptysis with jaundice',
                       'hemoptysis with cough',
                       'hemoptysis with fever',
                       'suffocation',
                       'breathing sound weakened',
                       'hemoptysis with skin and mucous membrane bleeding'],
        'idiopathic pulmonary fibrosis': ['one side of the chest collapsed',
                                          'respiratory failure',
                                          'appetite loss',
                                          'purulent sputum'],
        'desquamative interstitial pneumonia': ['heart failure',
                                                'weight loss',
                                                'appetite loss',
                                                'pneumatic dyspnea'],
        'idiopathic obstructive bronchiolitis with organizing pneumonia': ['fever',
                                                                           'cough with chest pain',
                                                                           'twirl pronunciation',
                                                                           'fever with cough'],
        'idiopathic hemosiderin': ['hemosiderinosis',
                                   'breathing difficulty',
                                   'internal bleeding',
                                   'weakness'],
        'exogenous allergic alveolitis': ['pulmonary interstitial fibrosis',
                                          'weight loss',
                                          'breathing difficulty',
                                          'chest tightness',
                                          'tachycardia'],
        'pediatric tuberculosis': ['herpes',
                                   'blood sputum',
                                   'tuberculosis',
                                   'lymph node tuberculosis',
                                   'nasal tuberculosis',
                                   'immune deficiency'],
        'pediatric acute bronchitis': ['wet voice',
                                       'fatigue',
                                       'bacterial infection',
                                       'diarrhea',
                                       'abdominal pain'],
        'pediatric influenza': ['child has stuffy nose',
                                'child has a red spot after fever',
                                'sickness',
                                'sleepiness',
                                'runny nose',
                                'dizziness',
                                'feeling cold'],
        'silicosis': ['barrel chest',
                      'appetite loss',
                      'exhalation sound extension',
                      'breathing sound weakened'],
        'neonatal asphyxia': ['newborn cyanosis',
                              'breathing inhibition',
                              'neonatal convulsions',
                              'breathing slow',
                              'neonatal heart failure'],
        'asthma': ['two lungs are diffuse or scattered',
                   'lung over-inflated',
                   'breathing difficulty',
                   'tracheal obstruction',
                   'cough',
                   'cough with wheezing'],
        'pediatric asthma': ['airway hyperresponsiveness',
                             'wheeze',
                             'nose fan',
                             'gas rush'],
        'pneumonia in children': ['drowsiness',
                                  'pale',
                                  'cough',
                                  'appetite is not good',
                                  'phlegm and sound',
                                  'irritable and uneasy',
                                  'cyanosis',
                                  'nose wing fan'],
        'cold': ['headaches',
                 'hot and cold',
                 'sore pain',
                 'fever',
                 'throat and burning sensation',
                 'nasal',
                 'fever with cold',
                 'flu'],
        'respiratory foreign body': ['respiratory stenosis',
                                     'sound hoarseness',
                                     'difficulty swallowing',
                                     'nails have large vertical stripes',
                                     'thyroglous can be touched underneath',
                                     'out of breath'],
        'respiratory bronchiole-associated interstitial lung disease': ['chest pain',
                                                                        'honeycomb lung',
                                                                        'hemoptysis'],
        'respiratory failure': ['upper pulmonary fibrosis',
                                'breathing difficulty',
                                'nails have large longitudinal lines',
                                'cardiac function suddenly decompensated',
                                'mixed acid-base balance disorder ',
                                'flap-like tremor'],
        'respiratory syncytial virus pneumonia': ['breathing difficulty',
                                                  'nasal stuffing'],
        'acute respiratory failure': ['cardiac arrest',
                                      'ring fingernail depression',
                                      'heart rate increase',
                                      'respiratory alkalosis',
                                      'gas diffusion disorder',
                                      'heart function suddenly decompensated'],
        'acute respiratory distress syndrome': ['coma',
                                                'respiratory failure',
                                                'increased lung texture',
                                                'lifting shoulders to help breathing',
                                                'respiratory alkalosis',
                                                'cardiac respiratory distress',
                                                'carbon dioxide retention'],
        'neonatal respiratory distress syndrome': ['face cyanosis',
                                                   'breathing difficulty',
                                                   'acute dyspnea',
                                                   'newborn hairpin',
                                                   'breath not rule',
                                                   'lip hair lividity'],
        'inhalation injury': ['moderate inhalation injury',
                              'mucosal congestion',
                              'breathing difficulty',
                              'wandering sound',
                              'breathing block',
                              'breathing low',
                              'tracheal tract sudden damage above',
                              'throat edema'],
        'pediatric cold': ['weak',
                           'pediatric nasal congestion',
                           'sore pain',
                           'tank inflammation',
                           'nasal stuff'],
        'congenital pulmonary cyst': ['purple lips', 'hemoptysis', 'purulent sputum']
    }

        symptom_l = tracker.get_slot("symptoms")
        symptom_l = [symptom.lower() for symptom in symptom_l]
        if len(symptom_l)<2:
            dispatcher.utter_message(text=f"Please enter some more symptoms.")
        else:
            print(symptom_l)
            intent = ''#symptom_l = ['cold', 'headache']
            flag = 0
            for key in d.keys():#all disease names
                if (all(x in d[key] for x in symptom_l)):
                    flag = 1
                    intent = key
                    break
            if flag == 1 : 
                dispatcher.utter_message(text=f"You probably have a disease called '{intent}'.")
                dispatcher.utter_message(text="You may be experiencing some of these symptoms:\n \n")
                for s in d[intent]:
                    dispatcher.utter_message(text=f"{s} ")
                dispatcher.utter_message(text="Would you like to more about this disease?")
            else:
                dispatcher.utter_message(text=f"I could not understand. Please provide more symptoms or contact a doctor.")
        # print(symptom_l)
        # dispatcher.utter_message(text=f"You have {symptom_l}")
        
        # for blob in tracker.latest_message['entities']:
        #     print(tracker.latest_message)
        #     if blob['entity'] == 'symptom':
        #         name = blob['value']
        #         if name in self.knowledge:
        #             dispatcher.utter_message(text = f'Yes, {name}' )
        #         else:
        #             dispatcher.utter_message(text = f'No, {name}' )
        
        # symptom_list = tracker.get_slot("symptoms")
        # intent = self.intent_mapper(symptom_list)
        # dispatcher.utter_message(text=intent)

        return []
