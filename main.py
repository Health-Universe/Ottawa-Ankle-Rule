import streamlit as st

# App Description
st.title('Ottawa Ankle Rule Calculator')
st.write("""
This Streamlit application helps medical professionals to determine the likelihood of a fracture in the ankle or foot using the Ottawa Ankle Rules. 
The Ottawa Ankle Rules are a set of guidelines for clinicians to help decide if a patient with foot or ankle pain should be offered X-ray imaging to diagnose a possible bone fracture.
""")

# Input fields
st.subheader('Patient Details')
has_foot_pain_or_tenderness = st.radio('Does the patient have pain in the malleolar zone?', ['Yes', 'No'])
has_bone_tenderness_at_posterior_edge = st.radio('Does the patient have bone tenderness at the posterior edge of the tibia or tip of the medial malleolus?', ['Yes', 'No'])
has_bone_tenderness_at_base_of_5th_metatarsal = st.radio('Does the patient have bone tenderness at the base of the 5th metatarsal?', ['Yes', 'No'])
can_bear_weight_and_walk_four_steps = st.radio('Can the patient bear weight both immediately and in the emergency department for four steps?', ['Yes', 'No'])

# Ottawa Ankle Rule Calculation
def check_ottawa_rules(foot_pain, bone_tenderness, bone_tenderness_5th, bear_weight):
    if foot_pain == 'Yes' and (bone_tenderness == 'Yes' or bone_tenderness_5th == 'Yes') and bear_weight == 'No':
        return 'Positive: Indication for X-ray.'
    else:
        return 'Negative: X-ray might not be necessary. Further evaluation required.'

# Display results
st.subheader('Results')
result = check_ottawa_rules(has_foot_pain_or_tenderness, has_bone_tenderness_at_posterior_edge, has_bone_tenderness_at_base_of_5th_metatarsal, can_bear_weight_and_walk_four_steps)
st.write(result)

st.write("""
## Usage Instructions
* Select the appropriate answers for the patient's condition in the given fields.
* The results will be displayed instantly below, indicating whether an X-ray is suggested according to the Ottawa Ankle Rules.
* Please note, this is only a guide and cannot replace professional medical advice.
""")
