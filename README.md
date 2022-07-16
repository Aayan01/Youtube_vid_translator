# Youtube_vid_translator
Project implements MLIR & Document translation. 

# Imported Libraries
Streamlit: Running Streamlit
Youtube transcript API:  Extracting Transcript from YouTube
Deep_translator-> googleTranslator: Translation and the Audio stuff
Gtts: Text -> Speech

#Steps
1. Input Video Link -> Display Video and Title


2. Select a language preference: done using language_dict 
3. If the “Translate” button is clicked: 
  a. Print “Translate Success”. 
  b. Generate Transcript: calling the function “generate_transcript(id)”
    i. Get the transcripts of the video from Youtube using the YouTubeTranscriptApi.get_transcript(id)API. 
   ii. Get all the text in the transcript to an empty string (in this case- “script”)
  c. Translate the Transcript into the language of given preference. And Print it into the Streamlit page.
  d. Generate Audio: Check if the chosen language is supported by Google Text-to-Speech.  
    i. If NO: Show a warning sign saying “Audio Support for this language is currently unavailable”.
   ii. If YES: 
      1. Convert translated script to speech audio using the gTTS library.  
      2. Save the speech, then open it in read-only binary format, read that audio file, and store it to be played on the Streamlit page. 

