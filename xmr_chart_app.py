import pandas as pd
import numpy as np
import plotly.express as px # Interactive charts
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image
import os

im = "📈"
st.set_page_config(
    page_title="XmR Chart App",
    page_icon=im,
    initial_sidebar_state='expanded',
    layout="wide"
)

st.title("The XmR Chart: The Most Useful Type of Process Behavior Chart")

st.markdown("### A project from [The Broken Quality Initiative](https://www.brokenquality.com/)")

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("# About the project")
    st.markdown(
        """
        The XmR chart app is part of a larger body of work called [**The Broken Quality Initiative**](https://www.brokenquality.com/). This 
        initiative teaches engineers how to reduce costs and improve quality by understanding variation. As the Swiss Army knife of process behavior
        charts, the XmR chart plays a seminal role in this task. It replaces the gut feelings and guess work of other methods with a reliable way to
        reduce costs and improve quality.

        To learn more about the XmR chart and build your understanding of variation visit [BrokenQuality.com](https://www.brokenquality.com/taguchi-loss-function).
        """
    )

    st.image("figures/Broken_quality_logo.png", use_container_width=True)

    st.markdown("# About the author")
    st.markdown(
        """
        [Jim Lehner](https://www.linkedin.com/in/jim-lehner/) is a graduate of Worcester Polytechnic Institute (WPI), with an undergraduate degree in mechanical engineering and a graduate degree in 
        manufacturing engineering. His professional experience and personal interests that place him at the confluence of manufacturing, data analytics, mechanical 
        engineering, and quality improvement. This has allowed Jim to reduced costs and improved quality in the automotive, medical device, aerospace, and defense 
        industries. The unifying feature to Jim's success, regardless of the industry, is his hands-on mentality and deep understanding of variation.
        """
    )
    st.markdown("# Contact")
    st.markdown(
        """
        Have questions or want to collaborate? Email James.Lehner@gmail.com or QualityIsBroken@gmail.com
        """
    )

    st.markdown("# The Socials")
    st.markdown(
        """
        [Linkedin](https://www.linkedin.com/in/jim-lehner/)
        [Substack](https://substack.com/@jimlehner)
        [BlueSky](https://bsky.app/profile/lehnro.bsky.social)
        """
    )

    st.markdown("# Website")
    st.markdown(
        """
        [BrokenQuality.com](www.BrokenQuality.com)
        """
    )

# --- XMR CHART ---
# st.markdown("## Introduction")

with st.expander("Click for an introduction to XmR charts"):
    st.markdown("## XmR Chart Overview")

    st.markdown(
        """
        When a dataset is composed of logically comparable individual values that retain their time-ordered sequence, and they are the 
        by-product of a process or system, the most effective tool for making sense of this data is the XmR chart. The XmR chart 
        specifically, and process behavior charts generally, are the only tools capable of making the invisible world of variation visible. 
        By characterizing process behavior as predictable or unpredictable using calculated process limits, process behavior charts allow 
        us to determine when it is economical to take actions to improve a process and when it is economical to leave a process alone.
        """
    )

    _, col_mid, _ = st.columns([0.75, 2, 0.75])

    with col_mid:
        st.image("figures/Fig_xmr_chart_app_figure_1.png", use_container_width=True,
                 caption="Figure 1. What do you want to accomplish?")

    st.markdown(
        """
        XmR charts are composed of two subplots, the chart of individual values—the X chart—and the chart of the associated moving ranges—the 
        mR chart. The defining features of these charts are the three calculated process limits: the Upper Process Limit (UPL), the Lower 
        Process Limit (LPL), and the Upper Range Limit (URL). The UPL and LPL define how large or small a value must be before it represents a 
        departure from the historic mean on the X chart. The URL defines how large a moving range must be before it represents a departure 
        from the average moving range.
        """
    )

    _, col_mid, _ = st.columns([0.75, 2, 0.75])

    with col_mid:
        st.image("figures/Fig_xmr_chart_example.png", use_container_width=True, 
                 caption="Figure 2. A simple XmR chart.")

    st.markdown(
        """
        When one or more values on an XmR chart is greater than the UPL, less than the LPL, greater than the URL, or some combination of all 
        three, this is evidence that both common causes of routine variation and assignable causes of exceptional variation influence process 
        behavior. In these instances, the underlying causal system is characterized as unpredictable. To improve an unpredictable process the 
        assignable causes of exceptional variation must be eliminated. Although few in number, they are dominant in their effect. They cause a 
        process to bounce and shift in unpredictable ways. This unpredictable behavior will continue until the assignable causes are eliminated.

        When all of the values on an XmR chart fall within the process limits, this is evidence that only common causes of routine variation 
        influence process behavior. In these instances, the underlying causal system is characterized as predictable because, although common 
        causes are many in number, they are minimal in their effect. If deemed economically viable, the improvement of a predictable process 
        requires reengineering. This is achieved through the introduction of new technology, new equipment, new materials, and new procedures. 
        Although this is contrary to conventional wisdom, it has been proven in practice time and time again.
        """
    )

    _, col_mid, _ = st.columns([0.5, 2, 0.5])

    with col_mid:
        st.image("figures/Fig_is_all_the_data_within_limits.png", use_container_width=True, 
                 caption="Figure 3. When one or more values fall outside the process limits, a process is characterized as unpredictable. " \
                 "When all values fall inside the process limits, a process is characterized as predictable.")


    st.markdown(
        """
        Process behavior charts generally, and the XmR chart specifically, are an operational definition for how to operate a process at its full 
        potential (high yield and low cost). By discriminating between the two types of variation they make the invisible world of variation 
        visible. When used in this way, the process behavior chart becomes a locomotive for continuous improvement. It ensures that, rather than 
        waste time performing an FMEA, improving the measurement process, or brainstorming what problem to work on, you let the process tell you 
        what to fix and when to fix it. No other tool is more capable or competent in this task. 
        
        To learn more about process behavior charts visit [BrokenQuality.com](https://www.brokenquality.com/).
        """
    )

with st.expander("Click to learn how to calculate process limits for an XmR chart"):
    st.markdown("## How are process limits calculated?")

    st.markdown(
        """
        The defining features of the XmR chart are the Upper Process Limit (UPL), Lower Process Limit (LPL), and Upper Range Limit (URL). Also 
        alled three sigma limits, natural process limits, or control limits, the process limits approximate what a process can achieve when it 
        is operated at its full potential. 

        The process limits for an XmR chart are calculated using the formulas: 
        """
    )

    _, col_mid, _ = st.columns([0.75, 2, 0.75])

    with col_mid:
        st.image("figures/EQ_process_limits.png", use_container_width=True)

    st.markdown(
        """
        Here, X-bar is the mean of the process data, mR-bar is the average moving range, and 2.660 and 3.268 are scaling factors. The 2.660 
        scaling factor, also represented as E2, is required to convert the average moving range into the appropriate amount of spread for the 
        individual values. The 3.268 scaling factor, also represented as D4, is required to convert the average moving range into an appropriate 
        upper bound for the moving ranges. When working with a dataset composed of logically comparable individual values, as is the case when 
        constructing an XmR chart, the effective subgroup size is n = 2. Thus, the E2 and D4 scaling factors will always assume values of 2.660 
        and 3.268, respectively.

        To learn how to build an XmR chart [click here](https://www.brokenquality.com/how-to-build-an-xmr-chart).

        To learn more about the origins of these scaling factors see Chapters 16.2 and 16.3 in [The Virus of Variation: Making Sense of Death and 
        Data using Process Behavior Charts](https://www.brokenquality.com/book).
        """
    )

    col_first, col_mid, col_last = st.columns([2, 2, 2])

    with col_mid:
        st.image("figures/virus_of_variation_book_cover_cropped.png", use_container_width=True)

with st.expander("Click to learn the origins of the term process behavior chart"):
    st.markdown("## A transition in nomenclature")

    st.markdown(
        """
        Control chart and process behavior chart are two terms that describe the same set of tools. The nomenclature transition from control chart 
        to process behavior chart originates from the statistician and quality control expert Donald J. Wheeler (Visit [SPCPress.com](https://www.spcpress.com/) to learn more). In his book 
        Understanding Variation: The Key to Managing Chaos, Wheeler notes that:
        """
    )

    st.markdown("""
    <blockquote style="border-left: 4px solid #ccc; padding-left: 1rem; color: #1a1a1a; font-style: italic;">
        <strong>Because of the baggage associated with the word 'control' this name [control chart] can be quite misleading.<br>
        Therefore we shall use the more descriptive name of process behavior chart to describe this versatile technique.<br></strong>
    </blockquote>
    """, unsafe_allow_html=True)

    st.markdown(
            """
            Wheeler’s statement is a recognition that the language we use matters. Control chart conjures the illusion of control. It insinuates that 
            the tool is responsible for controlling a process. As a result, this versatile tool is often relegated to the menial task of monitoring process 
            behavior. While the process behavior chart can certainly be used for this task its more effective use is in the solving of manufacturing problems. 
            Process behavior charts allow us to anticipate future process behavior based on the past. They give processes a voice that directs our time and attention 
            to where they are needed most. The term 'process behavior chart' is a more accurate description of this utility and why it is preferred over 'control chart'. 
            """
        )

st.markdown("## Instructions")

if "default_tick_interval" not in st.session_state:
    st.session_state.default_tick_interval = 5

# --- FALLBACK DEFAULTS ---
data = None
stage_column = None
label_column = None
selected_file = "None"

# --- SELECT OR UPLOAD A DATASET ---
dataset_columns = {
    "automated_manufacturing_part_lengths.csv": {
        "name": "Automated Manufacturing Part Lengths", 
        "data": "Value (mm)", 
        "label": "Sample", 
        "stage": None, 
        "tick_interval": 2,
        "description": "This dataset contains 60 part length measurements from an automated manufacturing line."
        },
    "manufacturing_PMI.csv": {
        "name": "Manufacturing PMI (Purchase Manager's Index)", 
        "data": "Manufacturing PMI", 
        "label": "Month", 
        "stage": None, 
        "tick_interval": 1,
        "description": "This dataset contains monthly manufacturing PMIs (Purchase Manager's Index) from February 2025 to January 2026."
        },
    "millikans_electron_charge_observations.csv": {
        "name": "Millikan's Electron Charge Observations", 
        "data": "Value", 
        "label": "Sample", 
        "stage": None, 
        "tick_interval": 5,
        "description": "This dataset contains 58 electron charge measurements (in coloumbs) made by Millikan."
        },
    "monthly_united_states_trade_deficits_2024.csv": {
        "name": "Monthly United States Trade Deficits 2024", 
        "data": "Value ($ billions)", 
        "label": "Month", 
        "stage": None, 
        "tick_interval": 1,
        "description": "This dataset contains the monthly tade deficits for the united states in 2024."
        },
    "OP200_weekly_first_pass_yield.csv": {
        "name": "OP200 Weekly First Pass Yield", 
        "data": "First-Pass Yield (%)", 
        "label": "Week", 
        "stage": None, 
        "tick_interval": 1,
        "description": "This dataset contains the first-pass yield for operation 200 (OP200) for a period of 24 weeks."
        },
    "quarterly_sales_by_region.csv": {
        "name": "Quarterly Sales by Region", 
        "data": "Sales", 
        "label": "Quarter", 
        "stage": "Stage", 
        "tick_interval": 5,
        "description": "This dataset contains the quarterly sales for 6 sales regions for 20 consecuitve quarters."
        },
    "shewharts_resistance_measurements.csv": {
        "name": "Shewhart's Resistance Measurements", 
        "data": "Resistance", 
        "label": "Value", 
        "stage": "Stage", 
        "tick_interval": 11,
        "description": "This dataset contains two sets of electrical resistance measurements collected by Walter A. Shewhart at Bell Telephone Laboratories."
        "The first set of measurements, called the 'Initial' stage, were collected before process improvements. The second set of measurements, called the 'Additional' "
        "stage, were collected after process improvements."
        },
    "vienna_general_death_to_birth_rates.csv": {
        "name": "Vienna General Death-to-Birth Rates", 
        "data": "Rate", 
        "label": "MonthYear", 
        "stage": "Stage", 
        "tick_interval": 6,
        "description": "This dataset contains the death-to-birth rates at Vienna General Hospital from January 1841 to March 1849. By dividing the dataset according to "
        "the implementation of Ignaz Semmelweis's handwashing policy, the impact of the policy is qualitatively and quantitaively visualized. "
        "To learn more about this dataset and the work of Ignaz Semmelweis read [The Virus of Variation: Making Sense of Death and Data using Process Behavior Charts](https://www.brokenquality.com/book)."
        },
    "wafer_assembly_part_placement.csv": {
        "name": "Wafer Assembly Part Placement",
        "data": "X position", 
        "label": "Sample", 
        "stage": "Stage", 
        "tick_interval": 10,
        "description": "This dataset contains part placement measurements from an automated pick-and-place manufacturing line. The values provided "
        "are the x-coordinates for wafer placement relative to a welded plate assembly."
        },
}

# Build display name to filename mapping
name_to_file = {v["name"]: k for k, v in dataset_columns.items()}
selected_name = st.selectbox("Select a sample dataset", ["None"] + list(name_to_file.keys()))
selected_file = name_to_file.get(selected_name, "None")

# Then offer file upload
uploaded_file = st.file_uploader("Or upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    col1_upload, col2_upload, col3_upload = st.columns(3)
    data_column = col1_upload.selectbox("Select the data column of the uploaded CSV", [None] + list(df.columns), index=0)
    label_column = col2_upload.selectbox("Select the label column of the uploaded CSV", [None, "Default (1 to n)"] + list(df.columns), index=0)
    stage_column = col3_upload.selectbox("Select the stage column of the uploaded CSV (if applicable)", ["Not Applicable"] + list(df.columns), index=0)

    if stage_column == "Not Applicable":
        stage_column = None

    if data_column is None and label_column is None:
        st.warning("Please select a data column and a label column.")
        st.stop()
    elif data_column is None:
        st.warning("Please select a data column.")
        st.stop()
    elif label_column is None:
        st.warning("Please select a label column.")
        st.stop()

    data = df[data_column].dropna()
    
    if label_column == "Default (1 to n)":
        label_column_data = list(range(1, len(df) + 1))
    else:
        label_column_data = df[label_column].tolist()

    data = df[data_column].dropna()
    mean = data.mean()
    std = data.std()

elif selected_file != "None":
    df = pd.read_csv(f"data/{selected_file}")

    description = dataset_columns.get(selected_file, {}).get("description", None)

    if description:
        st.markdown(f"## Selected dataset: {dataset_columns[selected_file]['name']}")
        st.markdown(description)
    
    col1, col2, col3 = st.columns(3)

    default_data = dataset_columns.get(selected_file, {}).get("data", None)
    default_label = dataset_columns.get(selected_file, {}).get("label", None)
    default_stage = dataset_columns.get(selected_file, {}).get("stage", None)
    st.session_state.default_tick_interval = dataset_columns.get(selected_file, {}).get("tick_interval", 5)
    st.session_state.tick_interval = st.session_state.default_tick_interval

    default_data_index = list(df.columns).index(default_data) if default_data in df.columns else None
    default_label_index = list(df.columns).index(default_label) if default_label in df.columns else None
    default_stage_index = list(df.columns).index(default_stage) if default_stage in df.columns else None

    data_column = col1.selectbox("Select the data column", df.columns, index=default_data_index, placeholder="None")
    label_column = col2.selectbox("Select the label column", df.columns, index=default_label_index, placeholder="None")
    stage_column = col3.selectbox("Select the stage column", [None] + list(df.columns), index=default_stage_index, placeholder="None")

    data = df[data_column].dropna().reset_index(drop=True)
    mean = data.mean()
    std = data.std()

    label_column_data = df[label_column].tolist()

if data is None:
    st.stop()

st.divider()


# --- XMR CHART DISPLAY CONTROLS ---
st.markdown("## XmR Chart Display Controls")

with st.expander("XmR Chart Display Controls"):
    col4, col5, col6 = st.columns(3)

    tick_interval = col4.number_input("Tick Interval (X)", min_value=1, step=1, key="tick_interval")
    round_value = col5.number_input("Number of Decimal Places", min_value=0, value=1, step=1, key="rounding_value")
    tick_angle = col6.number_input("X-Axis Tick Label Angle", min_value=0, value=0, step=15)

    col7, col8, col9, col10, col11 = st.columns(5)
    show_limits = col7.checkbox("Show Process Limits", value=True, help="Shows the process limits on the XmR chart.")
    show_annotations = col8.checkbox("Show Annotations", value=True, help="Show the process limit and central line annotations.")
    show_lines = col9.checkbox("Show Connecting Lines", value=True, help="Shows the lines connecting the values in the XmR chart.")
    bound_UPL = col10.checkbox("Bound UPL", value=False, help="Prevents UPL from exceeding 100% when data is composed of percentages.")
    bound_LPL = col11.checkbox("Bound LPL", value=True, help="Prevents LPL from being less than zero.")

line_mode = "lines+markers" if show_lines else "markers"

# --- QUESTIONS ---
dataset_questions = {
    # Automated Manufacturing Line Part Lengths
    "automated_manufacturing_part_lengths.csv": [
        {
            "question": "Based on the XmR chart of part lengths, how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Unpredictable, multiple values fall outside the process limits", 
                        "Based on the information provided I can't say"],
            "answer": "Unpredictable, multiple values fall outside the process limits",
            "explanation": "With several values falling outside the process limits the process is characterized as unpredictable.",
            "key": "auto_mfg_q1"
        },
        {
            "question": "Based on the XmR chart of part lengths, how many values are equal to the Lower Process Limit (LPL)?",
            "options": ["There is 1 value equal to the LPL",
                        "There is 1 value greater than the UPL", 
                        "There are 5 values equal to the LPL", 
                        "There are 4 values equal to the LPL"],
            "answer": "There are 4 values equal to the LPL",
            "explanation": "There are 4 values equal to the LPL of zero.",
            "key": "auto_mfg_q1a"
        },
        {
            "question": "Based on the XmR chart of part lengths, how many moving ranges are greater than the Upper Range Limit (URL)?",
            "options": ["There is 1 moving range greater than the URL",
                        "There is 1 moving range greater than the UPL", 
                        "There are 5 moving ranges greater than the URL", 
                        "There are 4 moving ranges equal to the URL"],
            "answer": "There is 1 moving range greater than the URL",
            "explanation": "There is 1 moving range greater than the URL.",
            "key": "auto_mfg_q1b"
        },
        {
            "question": "What does a value outside of the limits indicate?",
            "options": ["Only common causes of routine variation influence process behavior", 
                        "Only assignable causes of exceptional variation influence process behavior", 
                        "Both common causes of routine variation and assignable causes of exceptional variation influence process behavior", 
                        "It doesn't indicate anything"],
            "answer": "Both common causes of routine variation and assignable causes of exceptional variation influence process behavior",
            "explanation": "When one or more values fall outside the process limits it indicates that both common causes of routine variation and assignable causes of exceptional"
            "variation influence process behavior.",
            "key": "auto_mfg_q2"
        },
        {
            "question": "How is the X chart different from the mR chart?",
            "options": ["The X chart plots moving ranges, while the mR chart plots the individual values (actual observations)", 
                        "The X chart plots the individual values (actual observations), while the mR chart plots the moving ranges", 
                        "There is no difference—they plot the same thing", 
                        "They both plot the same thing"],
            "answer": "The X chart plots the individual values (actual observations), while the mR chart plots the moving ranges",
            "explanation": "The X chart plots the individual values, which are the actual observations or measurements, while the mR chart plots "
            "the absolute value of the difference between individual values called the moving ranges.",
            "key": "auto_mfg_q2a"
        },
        {
            "question": "What actions should be taken to improve this process?",
            "options": ["Mitigate the influence of common causes of routine variation", 
                        "Eliminate the influence of assignable causes of exceptional variation", 
                        "Nothing, this process is fine", "Based on the information provided I can't say"],
            "answer": "Eliminate the influence of assignable causes of exceptional variation",
            "explanation": "Although assignable causes are few in number they are dominant in their effect. Thus, improvement of this process requires the "
            "elimination of assignable causes."
            "variation influence process behavior.",
            "key": "auto_mfg_q3"
        },
    ],

    # Manufacturing PMI
    "manufacturing_PMI.csv": [
        {
            "question": "Based on the XmR chart of monthly manufacturing PMIs, how would you characterize the behavior of this process?",
            "options": ["Unpredictable, multiple values fall outside the process limits", 
                        "Predictable, all points are within the process limits", 
                        "Based on the information provided I can't say"],
            "answer": "Unpredictable, multiple values fall outside the process limits",
            "explanation": "With 1 value greater than the UPL, the process is characterized as unpredictable.",
            "key": "auto_mfg_q4"
        },
        {
            "question": "Based on the XmR chart of monthly manufacturing PMIs, how many moving ranges are greater than the Upper Range Limit (URL)?",
            "options": ["There is 1 moving range greater than the URL", 
                        "0, none of the moving ranges is greater than the URL",
                        "There are 4 values greater than the URL",
                        "Based on the information provided I can't say"],
            "answer": "0, none of the moving ranges is greater than the URL",
            "explanation": "Although one of the individual values on the X chart is greater than the UPL, none of the moving ranges on the mR chart "
            "are greater than the URL.",
            "key": "auto_mfg_q4a"
        },
        {
            "question": "What does the XmR chart of manufacturing PMIs indicate about process behavior?",
            "options": ["It indicates that only common causes of routine variation influence process behavior", 
                        "It indicates that only assignable causes of exceptional variation influence process behavior", 
                        "It doesn't indicate anything", 
                        "It indicates that both common causes of routine variation and assignable causes of exceptional variation influence process behavior"],
            "answer": "It indicates that both common causes of routine variation and assignable causes of exceptional variation influence process behavior",
            "explanation": "With one value greater than the UPL this process is influenced by both common and assignable causes.",
            "key": "auto_mfg_q5"
        },
        {
            "question": "What actions should be taken to improve this process, if any?",
            "options": ["Mitigate the influence of common causes of routine variation", 
                        "Eliminate the influence of assignable causes of exceptional variation", 
                        "Understand what caused the increase in manufacturing PMI",
                        "Based on the information provided I can't say"],
            "answer": "Understand what caused the increase in manufacturing PMI",
            "explanation": "An increase in manufacturing PMI is an indicator that the manufacturing sector is expanding. Thus, efforts should "
            "be made to understand the underlying "
            "cause of the expansion so that they can be reinforced.",
            "key": "auto_mfg_q6"
        },
    ],

    # Millikan's electron charge observations
    "millikans_electron_charge_observations.csv": [
        {
            "question": "Based on the XmR chart of Millikan's electron charge observations, how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Unpredictable, multiple values fall outside the process limits", 
                        "Based on the information provided I can't say"],
            "answer": "Predictable, all points are within the process limits",
            "explanation": "With all values falling inside the process limits, the process is characterized as predictable.",
            "key": "auto_mfg_q7"
        },
        {
            "question": "What is the Upper Process Limit of Millikan's electron charge observations (to 4 decimal places)? "
            "Hint: Under the 'XmR Chart Display Controls' dropdown menu you can change the number of decmial places that are displayed with the 'Number of Decimal Places'"
            " input.",
            "options": ["The UPL is 0.0187 coulombs",
                        "The UPL is 4.8301 coulombs", 
                        "The UPL is 4.7308 coulombs", 
                        "The UPL is 0.0610 coulombs"],
            "answer": "The UPL is 4.8301 coulombs",
            "explanation": "The UPL is 4.8301 coulombs.",
            "key": "auto_mfg_q7a"
        },
        {
            "question": "What is the Upper Range Limit for the moving ranges associated with Millikan's electron charge observations (to 5 decimal places)? "
            "Hint: Under the 'XmR Chart Display Controls' dropdown menu you can change the number of decmial places that are displayed with the 'Number of Decimal Places'"
            " input.",
            "options": ["The URL is 0.01867 coulombs",
                        "The URL is 4.83012 coulombs", 
                        "The URL is 4.73081 coulombs", 
                        "The URL is 0.06100 coulombs"],
            "answer": "The URL is 0.06100 coulombs",
            "explanation": "The URL is 0.06100 coulombs.",
            "key": "auto_mfg_q7b"
        },
        {
            "question": "When all of the values fall within the process limits, what does this indicate about future process behavior?",
            "options": ["It indicates that assignable causes must be eliminated",
                        "It indicates that future behavior cannot be predicted within limits", 
                        "It doesn't indicate anything", 
                        "It indicates that future behavior can be predicted within the process limits"],
            "answer": "It indicates that future behavior can be predicted within the process limits",
            "explanation": "When all of the values on an XmR chart fall within the process limits, it indicates that future behavior can be predicted within those limits.",
            "key": "auto_mfg_q8"
        },
        {
            "question": "What actions (if any) should be taken to improve this process?",
            "options": ["Mitigate the influence of common causes of routine variation", 
                        "Eliminate the influence of assignable causes of exceptional variation", 
                        "Nothing, this process cannot be improved because it is observations (measurements) of a naturally occuring phenomenon", 
                        "Based on the information provided I can't say"],
            "answer": "Nothing, this process cannot be improved because it is observations (measurements) of a naturally occuring phenomenon",
            "explanation": "When a mechanical (or man made) process is influenced by only common causes of routine variation, improvement is only possible through reengineering "
            "(i.e., new technology, new techniques, "
            "new methods, and new materials). However, in this case, further improvement is not possible because Millikan was measuring a naturally occuring phenomenon. While improvements"
            " in the measurement system may increase the precision of the observations there is nothing we can do that will change the charge of electrons."
            "variation influence process behavior.",
            "key": "auto_mfg_q9"
        },
    ],

    # Monthly United States trade deficits in 2024
    "monthly_united_states_trade_deficits_2024.csv": [
        {
            "question": "Based on the XmR chart of monthly United States trade deficits in 2024, how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Based on the information provided I can't say",
                        "Unpredictable, a value falls outside the process limits",
                        ],
            "answer": "Unpredictable, a value falls outside the process limits",
            "explanation": "With one value greater than the UPL the process is characterized as unpredictable.",
            "key": "auto_mfg_q10"
        },
        {
            "question": "When one or more values fall outside the process limits, what does this indicate about future process behavior?",
            "options": ["It indicates that only common causes of routine variation influence process behavior", 
                        "It indicates that only assignable causes of exceptional variation influence process behavior", 
                        "It doesn't indicate anything", 
                        "It indicates that future behavior cannot be predicted within the process limits"],
            "answer": "It indicates that future behavior cannot be predicted within the process limits",
            "explanation": "When one or more values fall outside the process limits the influence of assignable causes makes it impossible to predict "
            "future process behavior within the process limits.",
            "key": "auto_mfg_q11"
        },
        {
            "question": "Based on the XmR chart of trade deficits, what was the average monthly deficit for the observed period?",
            "options": ["The average deficit was 95.1", 
                        "The average deficit was 76.5", 
                        "The average deficit was 57.8", 
                        "The average deficit was 22.9"],
            "answer": "The average deficit was 76.5",
            "explanation": "The average deficit for the observed period was 76.5.",
            "key": "auto_mfg_q12"
        },
        {
            "question": "For the XmR chart of trade deficits, how many values are greater than the Upper Range Limit (URL)?",
            "options": ["There is 1 value greater than the UPL", 
                        "There is 1 value greater than the URL", 
                        "There are 0 values greater than the URL", 
                        "Based on the information provided I can't say"],
            "answer": "There are 0 values greater than the URL",
            "explanation": "While there is one value greater than the Upper Process Limit (UPL) on the X chart, none of the values (0) are greater than"
            "the Upper Range Limit (URL) on the mR chart.",
            "key": "auto_mfg_q12a"
        },
    ],

    # OP200 Weekly First-Pass Yield
    "OP200_weekly_first_pass_yield.csv": [
        {
            "question": "Based on the XmR chart of weekly first-pass yields, how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Based on the information provided I can't say",
                        "Unpredictable, several values falls outside the process limits",
                        ],
            "answer": "Unpredictable, several values falls outside the process limits",
            "explanation": "Several values fall outside the process limits that characterize the process as unpredictable.",
            "key": "auto_mfg_q10a"
        },
        {
            "question": "When one or more values fall outside the process limits, what does this indicate about future process behavior?",
            "options": ["It indicates that only common causes of routine variation influence process behavior", 
                        "It indicates that only assignable causes of exceptional variation influence process behavior", 
                        "It doesn't indicate anything", 
                        "It indicates that future behavior cannot be predicted within the process limits"],
            "answer": "It indicates that future behavior cannot be predicted within the process limits",
            "explanation": "When one or more values fall outside the process limits the influence of assignable causes makes it impossible to predict "
            "future process behavior within the process limits.",
            "key": "auto_mfg_q11b"
        },
        {
            "question": "What was the average weekly first-pass yield for the observed period (to 2 decimal places)? Hint: You can change the number of "
            "decimals that are displayed in the 'XmR Chart Display Controls' dropdown menu.",
            "options": ["The average weekly first-pass yield was 91.02%", 
                        "The average weekly first-pass yield was 81.4%", 
                        "The average weekly first-pass yield was 81.42%", 
                        "The average weekly first-pass yield was 71.82"],
            "answer": "The average weekly first-pass yield was 81.42%",
            "explanation": "The average first-pass yield was 81.42%. However, because the process is characterized as unpredictable, this average is an "
            "inaccurate representation of what the process has done in the past and cannot be used to anticipate what it will do in the future. "
            "Only when a process is characterized as predictable does the calculated mean accurately represent past and future behavior.",
            "key": "auto_mfg_q12c"
        },
        {
            "question": "How many weekly first-pass yields are less than the Lower Process Limit (LPL)?",
            "options": ["There are 10 weekly first-pass yields that are less than the LPL", 
                        "There is 1 weekly first-pass yields that are less than the LPL", 
                        "There are 5 weekly first-pass yields that are less than the LPL", 
                        "None of the weekly first-pass yields (0) that are less than the LPL"],
            "answer": "There are 5 weekly first-pass yields that are less than the LPL",
            "explanation": "There are 5 weekly first-pass yields that are less than the LPL and 5 weekly first-pass yields that are greater than the UPL."
            "the Upper Range Limit (URL) on the mR chart.",
            "key": "auto_mfg_q12d"
        },
    ],

    # Quarterly Sales by Region
    "quarterly_sales_by_region.csv": [
        {
            "question": "Based on the XmR chart of the sales regions, how would you characterize the behavior of the sales process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Based on the information provided I can't say",
                        "Unpredictable, there are many values that fall outside the process limits",
                        ],
            "answer": "Unpredictable, there are many values that fall outside the process limits",
            "explanation": "With many values falling outside the process limits, the sales process is characterized as unpredictable. With this said, "
            "evaluating all of the sales regions in a single XmR chart doesn't make much sense. It is better to evaluate each sales region on its own and with respect "
            "to the others using 'Stages'.",
            "key": "auto_mfg_q13"
        },
        {
            "question": "Click the 'Stage View & Customization' dropdown menu and select the 'Show Stages' check mark. This will divide the sales data into unique sales regions. "
            "What sales regions are predictable and what sales regions are unpredictable?",
            "options": ["All of the sales regions are characterized as unpredictable", 
                        "All of the sales regions are characterized as predictable", 
                        "Sales regions A, C, and E are predictable, while regions B, D, and F are unpredictable.", 
                        "Sales regions A, C, and E are unpredictable, while regions B, D, and F are predictable."],
            "answer": "Sales regions A, C, and E are predictable, while regions B, D, and F are unpredictable.",
            "explanation": "Sales regions A, C, and E are predictable while regions B, D, and F are unpredictable. Using a stage-based view of multiple processes that use the "
            "same quality or performance metric allows the stages to be compared directly. This makes differenes in variation between the stages more clear.",
            "key": "auto_mfg_q14"
        },
        {
            "question": "Assume you are the director managing these sales regions. Based on the stage view, what sales region needs the most attention?",
            "options": ["Region B, the sales in this region appear to be declining rapidly",
                        "Region E, the sales in this region are slow and will continue to be slow if something isn't done", 
                        "Region F, the sales in this region are unpredictable although they have grown recently", 
                        "Region A, even though the sales in this region are predictable they display a lot of variation"],
            "answer": "Region B, the sales in this region appear to be declining rapidly",
            "explanation": "The downward slope and unpredictable characterization of region B indicates that questions need to be asked.",
            "key": "auto_mfg_q15"
        },
        {
            "question": "Of the three regions that are characterized as predictable (A, C and E), which region had the highest average sales for the observed period?",
            "options": ["Region A had the highest average sales", 
                        "Region C had the highest average sales", 
                        "Region E had the highest average sales", 
                        "Based on this chart I can't tell"],
            "answer": "Region C had the highest average sales",
            "explanation": "On an XmR chart, the solid black line is the average (mean) of the process data. Since the mean line for Region C is greater than the mean line "
            "for Regions A and E it had the highest average sales for the observed period.",
            "key": "auto_mfg_q16"
        },
    ],

    # Shewhart's resistance measurements
    "shewharts_resistance_measurements.csv": [
        {
            "question": "Based on the XmR chart of resistance measurements (without 'Show Stages' selected), how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits",
                        "Unpredictable, there are many values that fall outside the process limits", 
                        "Based on the information provided I can't say",
                        ],
            "answer": "Unpredictable, there are many values that fall outside the process limits",
            "explanation": "With many values falling outside the process limits, the process is characterized as unpredictable.",
            "key": "auto_mfg_q17"
        },
        {
            "question": "Click the 'Stage View & Customization' dropdown menu and select the 'Show Stages' check mark. This will divide the resistance measurements into two stages (Initial and Additional). "
            "What is the characterization of the two stages?",
            "options": ["Both stages are characterized as unpredictable", 
                        "Both stages are characterized as predictable", 
                        "The 'Initial' stage is characterized as predictable, while the 'Additional' stage is characterized as unpredictable", 
                        "The 'Initial' stage is characterized as unpredictable, while the 'Additional' stage is characterized as predictable"],
            "answer": "The 'Initial' stage is characterized as unpredictable, while the 'Additional' stage is characterized as predictable",
            "explanation": "The 'Initial' stage is characterized as unpredictable, while the 'Additional' stage is characterized as predictable."
            " fall inside the process limits characterizing it as predictable.",
            "key": "auto_mfg_q18"
        },
        {
            "question": "What can be said about the 'Additional' resistance measurements?",
            "options": ["Because the 'Additional' resistance measurements are characterized as predictable, future process behavior can be predicted within limits",
                        "Because the 'Additional' resistance measurements are characterized as unpredictable, future process behavior cannot be predicted within limits", 
                        "Based on the information provided I can't make any statements", 
                        "Only assignable causes of exceptional variation influence process behavior"],
            "answer": "Because the 'Additional' resistance measurements are characterized as predictable, future process behavior can be predicted within limits",
            "explanation": "When a process is characterized as predictable future process behavior can be predicted within the respective process limits.",
            "key": "auto_mfg_q19"
        },
        {
            "question": "What is the Lower Process Limit (LPL) for the 'Additional' resistance measurements?",
            "options": ["The LPL is 4922.8", 
                        "The LPL is 4417.8", 
                        "The LPL is 3912.8", 
                        "Based on this chart I can't tell"],
            "answer": "The LPL is 3912.8",
            "explanation": "The LPL is 3912.8. megaohms",
            "key": "auto_mfg_q20"
        },
    ],

        # Vienna General Death-to-Birth Rates
        "vienna_general_death_to_birth_rates.csv": [
        {
            "question": "Based on the XmR chart of death-to-birth rates (without 'Show Stages' selected), how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits",
                        "Unpredictable, there are many values that fall outside the process limits", 
                        "Based on the information provided I can't say",
                        ],
            "answer": "Unpredictable, there are many values that fall outside the process limits",
            "explanation": "With many values falling outside the process limits, the process is characterized as unpredictable.",
            "key": "auto_mfg_q21"
        },
        {
            "question": "Click the 'Stage Customization' dropdown menu and select the 'Show Stages' check mark. This will divide the death-to-birth rates into stages "
            "(Before Handwashing and After handwashing). What is the characterization of the two stages?",
            "options": ["Both stages are characterized as unpredictable", 
                        "Both stages are characterized as predictable", 
                        "The 'Before' stage is characterized as predictable, while the 'After' stage is characterized as unpredictable", 
                        "The 'Before' stage is characterized as unpredictable, while the 'After' stage is characterized as predictable"],
            "answer": "Both stages are characterized as unpredictable",
            "explanation": "With multiple values falling outside the process limits for both stages, they are characterized as unpredictable.",
            "key": "auto_mfg_q22"
        },
        {
            "question": "How did the variation change between the before handwashing stage and the after handwashing stage?",
            "options": ["The variation decreased",
                        "The variation increased", 
                        "Based on the information provided I can't say", 
                        "The variation stayed the same"],
            "answer": "The variation decreased",
            "explanation": "By comparing the width of the process limits from the the two stages it is obvious that the variation "
            "decreased after handwashing was introduced.",
            "key": "auto_mfg_q23"
        },
        {
            "question": "What is the Upper Process Limit (UPL) for the 'After handwashing' stage?",
            "options": ["The UPL is 2.1%", 
                        "The UPL is 4.8%", 
                        "The UPL is 0.0%", 
                        "Based on this chart I can't tell"],
            "answer": "The UPL is 4.8%",
            "explanation": "The UPL is 4.8\% for the 'After handwashing' stage.",
            "key": "auto_mfg_q24"
        },
        {
            "question": "How many values are equal to the Lower Process Limit (LPL) for the 'After handwashing' stage?",
            "options": ["3 values are equal to the LPL for the 'After handwashing' stage", 
                        "2 values are equal to the LPL for the 'After handwashing' stage", 
                        "5 values are equal to the LPL for the 'After handwashing' stage", 
                        "None of the values (0) are equal to the LPL for the 'After handwashing' stage"],
            "answer": "2 values are equal to the LPL for the 'After handwashing' stage",
            "explanation": "2 of the values are equal to the LPL in the 'After handwashing' stage.",
            "key": "auto_mfg_q24a"
        },
    ],

    # Wafer assembly part placement
    "wafer_assembly_part_placement.csv": [
        {
            "question": "Based on the XmR chart of wafer assembly part placements (without 'Show Stages' selected), how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits",
                        "Unpredictable, there are many values that fall outside the process limits", 
                        "Based on the information provided I can't say",
                        ],
            "answer": "Unpredictable, there are many values that fall outside the process limits",
            "explanation": "With many values falling outside the process limits, the process is characterized as unpredictable.",
            "key": "auto_mfg_q25"
        },
        {
            "question": "Click the 'Stage Customization' dropdown menu and select the 'Show Stages' check mark. This will divide the wafer assembly placement data into three stages "
            "(Baseline, Initial change, Secondary change). What is the characterization of the three stages?",
            "options": ["All stages are characterized as unpredictable", 
                        "All stages are characterized as predictable", 
                        "The 'Baseline' stage and 'Initial change' stage are characterized as predictable, while the 'After' stage is characterized as unpredictable", 
                        "The 'Baseline' stage and 'Initial change' stage are characterized as unpredictable, while the 'After' stage is characterized as predictable"],
            "answer": "All stages are characterized as unpredictable",
            "explanation": "The characterization of a process is a function of both the X chart and mR chart. Thus, while the X chart of the 'Secondary change' shows"
            " all values fall within the process limits there are two values on the asssociated mR chart that are greater than the URL.",
            "key": "auto_mfg_q26"
        },
        {
            "question": "What is the Upper Process Limit (UPL) for the stage labeled 'Secondary change' (to 2 decimal places)? Hint: You can change the number of decimal places in the "
            "'XmR Chart Display Controls' dropdown menu.",
            "options": ["The UPL is 1.00",
                        "The UPL is 0.77", 
                        "The UPL is 0.48", 
                        "The UPL is 1.06"],
            "answer": "The UPL is 1.06",
            "explanation": "The UPL is 1.06 units.",
            "key": "auto_mfg_q27"
        },
        {
            "question": "What is the Upper Range Limit (URL) for the stage labeled 'Secondary change' (to 2 decimal places)?",
            "options": ["The URL is 1.06",
                        "The URL is 0.11", 
                        "The URL is 0.36", 
                        "The URL is 0.40"],
            "answer": "The URL is 0.36",
            "explanation": "The URL is 0.36 units",
            "key": "auto_mfg_q28"
        },
    ],
}

if selected_file in dataset_questions:
    with st.expander("Questions to consider"):
        for q in dataset_questions[selected_file]:
            selected = st.radio(
                q["question"],
                index=None,
                options=q["options"],
                key=q["key"]
            )
            if selected == q["answer"]:
                st.success(f"✅ Correct! {q['explanation']}")
            elif selected is not None:
                st.error("❌ Not quite. Try again.")

# --- STAGE LABEL CUSTOMIZATION ---
# Fallback defaults
show_stages = False
show_stage_labels = True
custom_stage_labels = {}
stage_tick_intervals = {}

if stage_column is not None:
    stages = df[stage_column].reset_index(drop=True)
    unique_stages = stages.unique()

    with st.expander("Stage View & Customization"):
        st.markdown(
            """
            A stage is a distinct period of time in which a process was operated under different conditions. This can be the result of an intentional
            or unintential change to the underlying causal system. Evaluating a process in accordance with stages using XmR charts allows for direct
            visual comparison between the different stages. It reveals if and how much the variation has changed between stages as well as if there have 
            been any shifts in the mean.
            """
        )

        col9, col10, col11, col12 = st.columns([1,1,3,3])

        show_stages = col9.checkbox("Show Stages", value=False)
        show_stage_labels = col10.checkbox("Show Stage Labels", value=True)

        if show_stages:
            stage_cols = st.columns(len(unique_stages))
            for i, stage in enumerate(unique_stages):
                if show_stage_labels:
                    custom_stage_labels[stage] = stage_cols[i].text_input(
                        f"Stage {i+1} label",
                        value=str(stage),
                        key=f"stage_label_{selected_file}_{i}"
                    )
                stage_tick_intervals[stage] = stage_cols[i].number_input(
                    f"Stage {i+1} tick interval",
                    min_value=1,
                    value=tick_interval,
                    step=1,
                    key=f"stage_tick_{selected_file}_{i}"
                )
else:
    stages = None
    unique_stages = []


# --- CALCULATIONS ---
moving_range = abs(data.diff())
ave_mR = moving_range.mean()

UPL = mean + (2.660*ave_mR)
if bound_UPL:
    UPL = min(UPL, 100)

LPL = mean - (2.660*ave_mR)
if bound_LPL:
    LPL = max(0, LPL)
URL = 3.268*ave_mR


# --- XMR CHART PLOTTING ---
fig = make_subplots(rows=2, cols=1, vertical_spacing=0.05)

# Calculate global marker colors (used when show_stages is False)
if show_limits:
    if LPL <= 0:
        x_colors = ["#d72323" if v > UPL or v <= 0 else "steelblue" for v in data]
        x_line_colors = ["black" if v > UPL or v <= 0 else "steelblue" for v in data]
        x_sizes = [7 if v > UPL or v <= 0 else 6 for v in data]
    else:
        x_colors = ["#d72323" if v > UPL or v < LPL else "steelblue" for v in data]
        x_line_colors = ["black" if v > UPL or v < LPL else "steelblue" for v in data]
        x_sizes = [7 if v > UPL or v < LPL else 6 for v in data]
    mr_colors = ["#d72323" if v > URL else "steelblue" for v in moving_range]
    mr_line_colors = ["black" if v > URL else "steelblue" for v in moving_range]
    mr_sizes = [7 if v > URL else 6 for v in moving_range]
else:
    x_colors = ["steelblue"] * len(data)
    x_line_colors = ["steelblue"] * len(data)
    x_sizes = [6] * len(data)
    mr_colors = ["steelblue"] * len(moving_range)
    mr_line_colors = ["steelblue"] * len(moving_range)
    mr_sizes = [6] * len(moving_range)

if show_stages and stage_column is not None:
    for i, stage in enumerate(unique_stages):
        stage_mask = stages == stage
        stage_data = data[stage_mask].reset_index(drop=True)
        stage_x = [j+1 for j, m in enumerate(stage_mask) if m]

        stage_mean = stage_data.mean()
        stage_mR = abs(stage_data.diff())
        stage_ave_mR = stage_mR.mean()
        stage_UPL = stage_mean + (2.660 * stage_ave_mR)
        stage_LPL = max(0, stage_mean - (2.660 * stage_ave_mR))
        stage_URL = 3.268 * stage_ave_mR

        # Calculate colors per stage limits
        if show_limits:
            if stage_LPL <= 0:
                s_colors = ["#d72323" if v > stage_UPL or v <= 0 else "steelblue" for v in stage_data]
                s_line_colors = ["black" if v > stage_UPL or v <= 0 else "steelblue" for v in stage_data]
                s_sizes = [7 if v > stage_UPL or v <= 0 else 6 for v in stage_data]
            else:
                s_colors = ["#d72323" if v > stage_UPL or v < stage_LPL else "steelblue" for v in stage_data]
                s_line_colors = ["black" if v > stage_UPL or v < stage_LPL else "steelblue" for v in stage_data]
                s_sizes = [7 if v > stage_UPL or v < stage_LPL else 6 for v in stage_data]
            s_mr_colors = ["#d72323" if v > stage_URL else "steelblue" for v in stage_mR]
            s_mr_line_colors = ["black" if v > stage_URL else "steelblue" for v in stage_mR]
            s_mr_sizes = [7 if v > stage_URL else 6 for v in stage_mR]
        else:
            s_colors = ["steelblue"] * len(stage_data)
            s_line_colors = ["steelblue"] * len(stage_data)
            s_sizes = [6] * len(stage_data)
            s_mr_colors = ["steelblue"] * len(stage_data)
            s_mr_line_colors = ["steelblue"] * len(stage_data)
            s_mr_sizes = [6] * len(stage_data)

        fig.add_trace(go.Scatter(
            x=stage_x,
            y=stage_data,
            mode=line_mode,
            line=dict(color="steelblue", width=2),
            marker=dict(
                size=s_sizes,
                color=s_colors,
                line=dict(color=s_line_colors, width=1 if show_limits else 0)
            )
        ), row=1, col=1)

        stage_mr_x = stage_x[1:]
        stage_mr_vals = stage_mR[1:]

        fig.add_trace(go.Scatter(
            x=stage_mr_x,
            y=stage_mr_vals,
            mode=line_mode,
            line=dict(color="steelblue", width=2),
            marker=dict(
                size=s_mr_sizes[1:],
                color=s_mr_colors[1:],
                line=dict(color=s_mr_line_colors[1:], width=1 if show_limits else 0)
            )
        ), row=2, col=1)

else:
    # X chart - single trace
    fig.add_trace(go.Scatter(
        x=list(range(1, len(data) + 1)),
        y=data,
        mode=line_mode,
        line=dict(color="steelblue", width=2),
        marker=dict(size=x_sizes, color=x_colors, line=dict(color=x_line_colors,
                                                    width=1 if show_limits else 0))
    ), row=1, col=1)

    # mR chart - single trace
    fig.add_trace(go.Scatter(
        x=list(range(2, len(moving_range) + 1)),
        y=moving_range,
        mode=line_mode,
        line=dict(color="steelblue", width=2),
        marker=dict(size=mr_sizes, color=mr_colors, line=dict(color=mr_line_colors,
                                                    width=1 if show_limits else 0))
    ), row=2, col=1)


# --- ADD PROCESS LIMITS AND ANNOTATIONS ---
hlines = [
    {"y": mean, "line_dash": "solid", "line_color": "black", "row": 1},
    {"y": UPL,  "line_dash": "dash",  "line_color": "#d72323", "row": 1},
    {"y": LPL,  "line_dash": "dash",  "line_color": "#d72323", "row": 1},
    {"y": URL,  "line_dash": "dash",  "line_color": "#d72323", "row": 2},
    {"y": ave_mR, "line_dash": "solid", "line_color": "black", "row": 2},
]

if not show_stages:
    if show_limits:
        for hline in hlines:
            fig.add_hline(y=hline["y"], line_dash=hline["line_dash"], line_color=hline["line_color"], line_width=2, row=hline["row"], col=1)

        mean_annotation_text = f"X̄: {mean:.{round_value}f}"
        UPL_annotation_text = f"UPL: {UPL:.{round_value}f}"
        LPL_annotation_text = f"LPL: {LPL:.{round_value}f}"
        ave_mR_annotation_text = f"<span style='text-decoration:overline'>mR</span>: {ave_mR:.{round_value}f}"
        URL_annotation_text = f"URL: {URL:.{round_value}f}"

        annotations = [
            {"y": mean,   "text": mean_annotation_text,   "yref": "y1", "borderpad": 1},
            {"y": UPL,    "text": UPL_annotation_text,    "yref": "y1", "borderpad": 1},
            {"y": LPL,    "text": LPL_annotation_text,    "yref": "y1", "borderpad": 1},
            {"y": ave_mR, "text": ave_mR_annotation_text, "yref": "y2", "borderpad": 4.1},
            {"y": URL,    "text": URL_annotation_text,    "yref": "y2", "borderpad": 1},
        ]
        if show_annotations:
            for ann in annotations:
                fig.add_annotation(
                    xref="paper",
                    yref=ann["yref"],
                    x=1,
                    y=ann["y"],
                    text=ann["text"],
                    showarrow=False,
                    font=dict(color="black", size=16),
                    bgcolor="white",
                    bordercolor="black",
                    borderwidth=1,
                    borderpad=ann["borderpad"],
                    xanchor="right",
                    yanchor="middle"
                )

# --- STAGES ---
if show_stages and stage_column is not None:

    stages = df[stage_column].reset_index(drop=True)
    unique_stages = stages.unique()
    stage_boundaries = [i for i in range(1, len(stages)) if stages[i] != stages[i-1]]

    # Draw stage boundary lines
    for boundary in stage_boundaries:
        fig.add_vline(x=boundary + 0.5, line_dash="solid", line_color="black", line_width=1, row="all", col=1)

    # Add stage title annotations
    if show_stage_labels:
        for i, stage in enumerate(unique_stages):
            stage_mask = stages == stage
            stage_indices = [j for j, m in enumerate(stage_mask) if m]
            x_mid = (stage_indices[0] + stage_indices[-1]) / 2 + 1

            fig.add_annotation(
                xref="x",
                yref="paper",
                x=x_mid,
                y=1.05,
                text=f"<b>{custom_stage_labels[stage]}</b>",
                showarrow=False,
                font=dict(color="black", size=14),
                xanchor="center"
            )

    # Calculate and plot limits for each stage
    for i, stage in enumerate(unique_stages):
        stage_mask = stages == stage
        stage_data = data[stage_mask].reset_index(drop=True)
        stage_x = [j+1 for j, m in enumerate(stage_mask) if m]

        stage_mean = stage_data.mean()
        stage_mR = abs(stage_data.diff())
        stage_ave_mR = stage_mR.mean()
        stage_UPL = stage_mean + (2.660 * stage_ave_mR)
        stage_LPL = max(0, stage_mean - (2.660 * stage_ave_mR))
        stage_URL = 3.268 * stage_ave_mR

        gap = 1
        x_start = stage_x[0] + (gap if i > 0 else 0)
        x_end = stage_x[-1] - (gap if i < len(unique_stages) - 1 else 0)

        if show_limits:
            stage_hlines = [
                {"y": stage_mean,   "line_dash": "solid", "line_color": "black",   "row": 1},
                {"y": stage_UPL,    "line_dash": "dash",  "line_color": "#d72323", "row": 1},
                {"y": stage_LPL,    "line_dash": "dash",  "line_color": "#d72323", "row": 1},
                {"y": stage_URL,    "line_dash": "dash",  "line_color": "#d72323", "row": 2},
                {"y": stage_ave_mR, "line_dash": "solid", "line_color": "black",   "row": 2},
            ]

            for hl in stage_hlines:
                fig.add_shape(
                    type="line",
                    x0=x_start, x1=x_end,
                    y0=hl["y"], y1=hl["y"],
                    line=dict(dash=hl["line_dash"], color=hl["line_color"], width=2),
                    row=hl["row"], col=1
                )

            # Only show annotations for the last stage
            if show_annotations and i == len(unique_stages) - 1:
                stage_annotations = [
                    {"y": stage_mean,   "text": f"X̄: {stage_mean:.{round_value}f}", "yref": "y1", "borderpad": 1},
                    {"y": stage_UPL,    "text": f"UPL: {stage_UPL:.{round_value}f}", "yref": "y1", "borderpad": 1},
                    {"y": stage_LPL,    "text": f"LPL: {stage_LPL:.{round_value}f}", "yref": "y1", "borderpad": 1},
                    {"y": stage_ave_mR, "text": f"<span style='text-decoration:overline'>mR</span>: {stage_ave_mR:.{round_value}f}", "yref": "y2", "borderpad": 4.1},
                    {"y": stage_URL,    "text": f"URL: {stage_URL:.{round_value}f}", "yref": "y2", "borderpad": 1},
                ]

                for ann in stage_annotations:
                    fig.add_annotation(
                        xref="paper",
                        yref=ann["yref"],
                        x=1,
                        y=ann["y"],
                        text=ann["text"],
                        showarrow=False,
                        font=dict(color="black", size=16),
                        bgcolor="white",
                        bordercolor="black",
                        borderwidth=1,
                        borderpad=ann["borderpad"],
                        xanchor="right",
                        yanchor="middle"
                    )

elif show_stages and stage_column is None:
    st.warning("No stage column selected.")

if show_stages and stage_column is not None:
    stages = df[stage_column].reset_index(drop=True)
    stage_boundaries = [i for i in range(1, len(stages)) if stages[i] != stages[i-1]]
    
    for boundary in stage_boundaries:
        fig.add_vline(x=boundary + 0.5, line_dash="solid", line_color="black", line_width=1, row="all", col=1)

elif show_stages and stage_column is None:
    st.warning("No stage column selected.")

# --- LAYOUT ---
if show_stages and stage_column is not None:
    stage_tickvals = []
    stage_ticktext = []
    for stage in unique_stages:
        stage_mask = stages == stage
        stage_indices = [j for j, m in enumerate(stage_mask) if m]
        interval = stage_tick_intervals.get(stage, tick_interval)
        stage_tickvals += [stage_indices[k] + 1 for k in range(0, len(stage_indices), interval)]
        if label_column is not None:
            stage_ticktext += df[label_column].tolist()[stage_indices[0]:stage_indices[-1]+1:interval]
        else:
            stage_ticktext += [str(stage_indices[k] + 1) for k in range(0, len(stage_indices), interval)]

    fig.update_layout(
        xaxis=dict(
            tickvals=stage_tickvals,
            ticktext=stage_ticktext,
            tickangle=tick_angle
        )
    )
elif label_column is None:
    fig.update_layout(
        xaxis=dict(
            tick0=1,
            dtick=tick_interval,
            rangemode="nonnegative"
        )
    )
elif label_column is not None:
    fig.update_layout(
        xaxis=dict(
            tick0=1,
            tickvals=list(range(1, len(data) + 1, tick_interval)),
            ticktext=label_column_data[::tick_interval],
            tickangle=tick_angle,
        )
    )

fig.update_layout(
    height=800,
    showlegend=False,
    margin=dict(t=60),
    xaxis2=dict(showticklabels=False),
    yaxis=dict(title="Individual Value (X)"),
    yaxis2=dict(title="Moving Range (mR)")
)

st.plotly_chart(fig, use_container_width=True)