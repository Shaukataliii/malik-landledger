import streamlit as st
import pandas as pd
from gtts import gTTS

# setting configurations and data
st.set_page_config(page_title='LandLedger', page_icon=':green_book:', layout='centered')
session = st.session_state
headings_color = 'green'
df = pd.read_csv('malik-landledger-dummy.csv')


# creating UI
st.title(":green_book: Malik's LandLedger")
# st.caption('Your land, your legacy')
st.divider()

st.selectbox('Please select the way, you wanna search your land.', options = ['Khasra', 'Khewat'], key = 'search_type', label_visibility = 'hidden')
st.chat_input('Enter the khewat/khasra number here', key = 'number')


# creating backend
if session.number:
    # getting the entered search type and number
    type = session.search_type
    entered_number = int(session.number)

    # if type is khewat then getting the row by searching df specific column and then extracting the required data and storing in variables
    if type == 'Khewat':
        try:
            # st.write('Entered in if for khewat no')
            retrieved_row = df[df['khewat_nos'] == entered_number]
            owner_name = retrieved_row['owner_name'].iloc[0]
            khewat_khasras_list = retrieved_row['khewat_khasras_list'].iloc[0]
            khewat_rqbas = retrieved_row['khewat_rqbas'].iloc[0]
            rqba_pieces = str(khewat_rqbas).split('-')

            with st.spinner('Getting results...'):
                # preparing text and displaying audio using gTTS (google text to speech | free)
                audio = gTTS(f"{rqba_pieces[0]} کنال, {rqba_pieces[1]} مرلے, {rqba_pieces[2]} فٹ۔.", lang = 'ur')
                audio.save('audio.mp3')
                st.audio(data = open('audio.mp3', 'rb'), format = 'mp3')

                # writting the output using the variablels
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.write(f':{headings_color}[Khewat no.]')
                    st.write(str(entered_number))
                with col2:
                    st.write(f':{headings_color}[Owner]')
                    st.write(owner_name)
                with col3:
                    st.write(f':{headings_color}[Khasras]')
                    st.write(khewat_khasras_list)
                with col4:
                    st.write(f':{headings_color}[Area]')
                    st.write(khewat_rqbas)


        # Throwing sorry message if there is no record
        except:
            st.error('Sorry. You have no land in khewat no. {}'.format(entered_number))
            # st.audio(data = open('error-audio.mp3', 'rb'), format = 'mp3')

    # if type is not khewat i.e. khasra, then getting the row by searching df specific column and then extracting the required data and storing in variables
    else:
        try:
            # st.write('Entered in else block for khasra no.')
            retrieved_row = df[df['khasra_nos'] == entered_number]
            owner_name = retrieved_row['owner_name'].iloc[0]
            khasra_rqba = retrieved_row['khasra_rqbas'].iloc[0]
            rqba_pieces = str(khasra_rqba).split('-')

            with st.spinner('Getting results...'):
                # preparing text and displaying audio using gTTS (google text to speech | free)
                audio = gTTS(f"{rqba_pieces[0]} کنال, {rqba_pieces[1]} مرلے, {rqba_pieces[2]} فٹ۔.", lang = 'ur')
                audio.save('audio.mp3')
                st.audio(data = open('audio.mp3', 'rb'), format = 'mp3')

                # writting the output using the variablels
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f':{headings_color}[Khasra no.]')
                    st.write(str(entered_number))
                with col2:
                    st.write(f':{headings_color}[Owner]')
                    st.write(owner_name)
                with col3:
                    st.write(f':{headings_color}[Area]')
                    st.write(khasra_rqba)


        # Throwing sorry message if there is no record
        except:
            st.error('Sorry. You have no land in khasra no. {}'.format(entered_number))
            # st.audio(data = open('error-audio.mp3', 'rb'), format = 'mp3')



# code used for generating error audios
# khewat_err = gTTS('Sorry. You have no land in this.')
# khewat_err.save('error-audio.mp3')