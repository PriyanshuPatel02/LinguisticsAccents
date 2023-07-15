import os
from gtts import gTTS
import gradio as gr
from translate import Translator
# import speech_recognition as sr

os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

auth_token = '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'   # For accesing HugginFace Facebook Model. 

class Languages:
    """ Languages currently supported by the application. """

    lang = {'Afrikaans': 'af','Arabic':'ar','Bulgarian':'bg','Bengali':'bn','Bosnian':'bs',
    'Catalan':'ca','Czech':'cs','Danish':'da','German':'de','Greek':'el','English':'en',
    'Spanish':'es','Estonian':'et','Finnish':'fi','French':'fr','Gujarati':'gu','Hindi':'hi',
    'Croatian':'hr','Hungarian':'hu','Indonesian':'id','Icelandic':'is','Italian':'it',
    'Hebrew':'iw','Japanese':'ja','Javanese':'jw','Khmer':'km','Kannada':'kn','Korean':'ko',
    'Latin':'la','Latvian':'lv','Malayalam':'ml','Marathi':'mr','Malay':'ms',
    'Myanmar (Burmese)':'my','Nepali':'ne', 'Dutch':'nl','Norwegian':'no',
    'Polish':'pl','Portuguese':'pt','Romanian':'ro','Russian':'ru','Sinhala':'si',
    'Slovak':'sk', 'Albanian':'sq','Serbian':'sr','Sundanese':'su','Swedish':'sv',
    'Swahili':'sw','Tamil':'ta','Telugu':'te','Thai':'th','Filipino':'tl','Turkish':'tr',
    'Ukrainian':'uk','Urdu':'ur','Vietnamese':'vi','Chinese (Simplified)':'zh-CN',
    'Chinese (Mandarin/Taiwan)':'zh-TW',
    'Chinese (Mandarin)':'zh'}

class TLD:
    """ Depending on the top-level domain, gTTS can speak in different accents. """

    tld = {'English(Australia)':'com.au', 'English (United Kingdom)':'co.uk',
    'English (United States)':'us', 'English (Canada)':'ca','English (India)':'co.in',
    'English (Ireland)':'ie','English (South Africa)':'co.za','French (Canada)':'ca',
    'French (France)':'fr','Portuguese (Brazil)':'com.br','Portuguese (Portugal)':'pt',
    'Spanish (Mexico)':'com.mx','Spanish (Spain)':'es','Spanish (United States)':'us'}

langs = Languages()
top_level_domain = TLD()

""" [Utiility Functions] """

def T2TConversion(text, dest):
    """ [(Utility Function) : Converts sentence from english to another language ] """
    translator = Translator(to_lang=langs.lang[dest])
    return translator.translate(text)

class GRadioInterface:
    """ [Class for managing UI for the application.] """
    def __init__(self, function) -> None:
        """ [Interface for packaging GRadio Application] """
        
        # Necessary for interface
        self._function = function
        self._inputs = [ 
                gr.Text(label='Write a sentence in English'),
                gr.Dropdown([key for key,_ in langs.lang.items()])],
               
        self.outputs = gr.Text(label='The Converted Text'),

    
    
    def start(self):
        """ [Launching the interface in a tabbed manner.] """
          
        demo =  gr.Interface(fn=self._function, inputs = self._inputs,outputs= self.outputs)
        demo.launch()

demo_app = GRadioInterface(function=T2TConversion)
demo_app.start()
