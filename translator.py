# Importing Libraries

# Running Streamlit
from gtts import gTTS
from deep_translator import GoogleTranslator
from pytube import YouTube
from textwrap import dedent
from urllib.parse import urlparse
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
st.set_page_config(  # Added favicon and title to the web app
    page_title="IR Project",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Extracting Transcript from YouTube

# Translation and Audio stuff

st.sidebar.title("This is our IR Project")

# Get Key value from Dictionary


def get_key_from_dict(val, dic):
    key_list = list(dic.keys())
    val_list = list(dic.values())
    ind = val_list.index(val)
    return key_list[ind]
# -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x


# Input Video Link
url = st.sidebar.text_input(
    'Video URL', 'https://www.youtube.com/watch?v=9z8ujpPgUjI')

# Display Video and Title
yt = YouTube(url)
value = yt.title
st.info("### " + value)  # "###" - inc. title size. this line prints the title.
st.video(url)


# -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

# Select Language Preference
languages_dict = {'en': 'English', 'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (simplified)', 'zh-tw': 'Chinese (traditional)', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'he': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'ko': 'Korean',
                  'ku': 'Kurdish (kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'or': 'Odia', 'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'}
add_selectbox = st.sidebar.selectbox(
    "Select Language",
    ('English', 'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (simplified)', 'Chinese (traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean',
     'Kurdish (kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (burmese)', 'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')
)

# If Translate button is clicked
if st.sidebar.button('Translate'):
    st.success(dedent("""### \U0001F4D6 Translate
> Success!
    """))

    # Generate Transcript by slicing YouTube link to id- TO KNOW
    url_data = urlparse(url)
    id = url_data.query[2::]

    def generate_transcript(id):
        transcript = YouTubeTranscriptApi.get_transcript(id)
        script = ""

        for text in transcript:
            t = text["text"]
            if t != '[Music]':
                script += t + " "

        return script, len(script.split())

    transcript, no_of_words = generate_transcript(id)

    # Translate and Print
    translated = GoogleTranslator(source='auto', target=get_key_from_dict(
        add_selectbox, languages_dict)).translate(transcript)
    html_str3 = f"""
    <style>
    p.a {{
    text-align: justify;
    }}
    </style>
    <p class="a">{translated}</p>
    """
    st.markdown(html_str3, unsafe_allow_html=True)

    # Generate Audio
    st.success("###  \U0001F3A7 Hear your Text")
    no_support = ['Amharic', 'Azerbaijani', 'Basque', 'Belarusian', 'Cebuano', 'Chichewa', 'Chinese (simplified)', 'Chinese (traditional)', 'Corsican', 'Frisian', 'Galician', 'Georgian', 'Haitian creole', 'Hausa', 'Hawaiian', 'Hmong', 'Igbo', 'Irish', 'Kazakh', 'Kurdish (kurmanji)',
                  'Kyrgyz', 'Lao', 'Lithuanian', 'Luxembourgish', 'Malagasy', 'Maltese', 'Maori', 'Mongolian', 'Odia', 'Pashto', 'Persian', 'Punjabi', 'Samoan', 'Scots gaelic', 'Sesotho', 'Shona', 'Sindhi', 'Slovenian', 'Somali', 'Tajik', 'Uyghur', 'Uzbek', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']
    if add_selectbox in no_support:
        st.warning(
            " \U000026A0 \xa0 Audio Support for this language is currently unavailable\n")
        lang_warn = GoogleTranslator(source='auto', target=get_key_from_dict(add_selectbox, languages_dict)).translate(
            "\U000026A0 \xa0 Audio Support for this language is currently unavailable")
        st.warning(lang_warn)
    else:
        speech = gTTS(text=translated, lang=get_key_from_dict(
            add_selectbox, languages_dict), slow=False)
        speech.save('user_trans.mp3')
        # rb : Opens the file as read-only in binary format and starts reading from the beginning of the file.
        audio_file = open('user_trans.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg', start_time=0)
  
 #############################################################################################################################3
