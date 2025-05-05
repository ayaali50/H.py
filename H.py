import streamlit as st
import datetime

# تعديل شكل الصفحة والألوان
st.set_page_config(
    page_title="Genetic and Chronic Diseases App",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# خلفية وألوان مبهجة
page_bg_img = """
<style>
body {
background-color: #e0f7fa;
color: #00695c;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# عنوان رئيسي
st.title("🧬 Genetic and Chronic Diseases Explorer")
st.write("استكشاف شامل للأمراض الوراثية والمزمنة - Detailed medical insights.")

# خانة الموبايل أو الإيميل
st.sidebar.header("Set Reminder")
contact = st.sidebar.text_input("Enter your phone number or email (أدخل رقم هاتفك أو بريدك الإلكتروني):")
reminder_time = st.sidebar.time_input("Select reminder time (حدد وقت التذكير):", datetime.time(9, 0))

# قائمة الأمراض
diseases = [
    "Type 1 Diabetes",
    "Cystic Fibrosis",
    "Sickle Cell Anemia",
    "Hereditary Cancer",
    "Down Syndrome",
    "Aplastic Anemia",
    "Hereditary Blindness",
    "Wilson's Disease",
    "Multiple Sclerosis",
    "Lupus (SLE)",
    "Rheumatoid Arthritis",
    "Hypertension",
    "Asthma",
    "Type 2 Diabetes",
    "Autism Spectrum Disorder",
    "Schizophrenia",
    "Breast Cancer",
    "Alzheimer's Disease",
    "Amyotrophic Lateral Sclerosis (ALS)"
]

# اختيار المرض
selected_disease = st.selectbox("Choose a Disease (اختر مرضًا):", diseases)

# دالة عرض المعلومات
def show_disease_info(name):
    if name == "Type 1 Diabetes":
        st.header("Type 1 Diabetes (سكري النوع الأول)")
        st.subheader("Definition (تعريف):")
        st.write("Type 1 diabetes is a chronic condition in which the pancreas produces little or no insulin. It usually appears during childhood or adolescence.")
        st.write("سكري النوع الأول هو حالة مزمنة حيث ينتج البنكرياس القليل أو لا ينتج الإنسولين. يظهر عادة في الطفولة أو المراهقة.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Increased thirst (العطش الشديد)
        - Frequent urination (التبول المتكرر)
        - Hunger (الجوع)
        - Fatigue (التعب)
        - Blurred vision (تشوش الرؤية)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("An autoimmune destruction of insulin-producing beta cells in the pancreas triggered by genetic factors and possibly viruses.")
        st.write("تدمير مناعي ذاتي لخلايا بيتا المنتجة للإنسولين في البنكرياس، ناجم عن عوامل وراثية وربما فيروسات.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("""
        - Administer fast-acting sugar if low blood sugar suspected (تناول سكر سريع الامتصاص في حالة الاشتباه في انخفاض السكر).
        - Monitor blood glucose levels regularly (مراقبة مستويات السكر باستمرار).
        - Seek emergency help if unconsciousness occurs (طلب إسعاف في حالة فقدان الوعي).
        """)

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Autoimmune Genetic Disorder (اضطراب مناعي وراثي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with genes like HLA-DR3 and HLA-DR4, affecting immune response.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Maintain a consistent eating schedule and monitor your blood sugar before and after meals.")
        st.success("احرص على تناول وجبات منتظمة ومراقبة السكر قبل وبعد الأكل.")

    elif name == "Cystic Fibrosis":
        st.header("Cystic Fibrosis (التليف الكيسي)")
        st.subheader("Definition (تعريف):")
        st.write("A genetic disorder that affects the lungs, pancreas, and other organs, causing thick, sticky mucus production.")
        st.write("اضطراب جيني يؤثر على الرئتين والبنكرياس وأعضاء أخرى، ويسبب إنتاج مخاط سميك ولزج.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Chronic cough (سعال مزمن)
        - Difficulty breathing (صعوبة في التنفس)
        - Frequent lung infections (عدوى رئوية متكررة)
        - Poor growth (نمو ضعيف)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Caused by mutations in the CFTR gene, affecting chloride channels and leading to mucus buildup.")
        st.write("ينتج عن طفرات في جين CFTR تؤثر على قنوات الكلوريد وتؤدي إلى تراكم المخاط.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("""
        - Chest physiotherapy to clear mucus (العلاج الطبيعي للصدر لتنظيف المخاط).
        - Use of medications like bronchodilators (استخدام أدوية مثل موسعات الشعب الهوائية).
        - Seek medical advice for respiratory distress (طلب استشارة طبية في حالة ضيق التنفس).
        """)

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Genetic Disorder (اضطراب وراثي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Caused by mutations in the CFTR gene, leading to faulty chloride transport.")
        st.write("ناجم عن طفرات في جين CFTR مما يؤدي إلى النقل الخاطئ للكلوريد.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Early diagnosis and lung function monitoring are crucial for better management.")
        st.success("التشخيص المبكر ومراقبة وظائف الرئة أمران حاسمان لإدارة أفضل.")

    # (تكملة الأمراض الأخرى بنفس الطريقة)
    # نكمل باقي الأمراض بالطريقة نفسها

# عرض معلومات المرض
show_disease_info(selected_disease)
elif name == "Sickle Cell Anemia":
        st.header("Sickle Cell Anemia (الأنيميا المنجلية)")
        st.subheader("Definition (تعريف):")
        st.write("A genetic disorder affecting hemoglobin, causing red blood cells to become sickle-shaped and block blood flow.")
        st.write("اضطراب وراثي يؤثر على الهيموغلوبين، يجعل خلايا الدم الحمراء تأخذ شكل المنجل وتعيق تدفق الدم.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Pain episodes (نوبات ألم)\n- Fatigue (إرهاق)\n- Swelling (تورم)\n- Frequent infections (عدوى متكررة)")
        st.subheader("Causes (الأسباب):")
        st.write("Caused by mutation in the HBB gene on chromosome 11.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Hydration\n- Pain management\n- Emergency care for severe crises")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Genetic Blood Disorder (اضطراب دم وراثي)")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Caused by mutation in HBB gene.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Stay hydrated and avoid extreme temperatures.")
        st.success("اشرب الماء وتجنب درجات الحرارة القصوى.")

    elif name == "Hereditary Cancer":
        st.header("Hereditary Cancer (السرطان الوراثي)")
        st.subheader("Definition (تعريف):")
        st.write("Cancer that runs in families due to inherited gene mutations, often increasing the risk for specific cancer types.")
        st.write("سرطان ينتقل في العائلات بسبب طفرات جينية موروثة، غالبًا يزيد من خطر أنواع معينة.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Lumps\n- Fatigue\n- Weight loss\n- Depends on cancer type")
        st.subheader("Causes (الأسباب):")
        st.write("Mutations in genes like BRCA1, BRCA2, TP53.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Early screening\n- Regular checkups")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Genetic Disorder (اضطراب وراثي)")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Often related to mutations in BRCA1/2.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Consider genetic testing if you have a family history of cancer.")
        st.success("قم بالفحص الجيني إذا كان لديك تاريخ عائلي.")

    elif name == "Down Syndrome":
        st.header("Down Syndrome (متلازمة داون)")
        st.subheader("Definition (تعريف):")
        st.write("A chromosomal disorder caused by the presence of all or part of a third copy of chromosome 21.")
        st.write("اضطراب صبغي ناتج عن وجود نسخة ثالثة كلية أو جزئية من الكروموسوم 21.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Intellectual disability\n- Distinct facial features\n- Developmental delays")
        st.subheader("Causes (الأسباب):")
        st.write("Presence of an extra chromosome 21 (trisomy 21).")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Supportive care\n- Early intervention")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Chromosomal Disorder (خلل صبغي)")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Extra chromosome 21 causes Down Syndrome.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Early support and therapy improve quality of life.")
        st.success("الدعم المبكر يحسن جودة الحياة.")

    elif name == "Aplastic Anemia":
        st.header("Aplastic Anemia (فقر الدم اللاتنسجي)")
        st.subheader("Definition (تعريف):")
        st.write("A condition where the bone marrow fails to produce enough blood cells.")
        st.write("حالة يفشل فيها نخاع العظم في إنتاج ما يكفي من خلايا الدم.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Fatigue\n- Frequent infections\n- Easy bruising")
        st.subheader("Causes (الأسباب):")
        st.write("Can be genetic or acquired due to drugs, toxins, or infections.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Avoid infections\n- Seek medical help for bleeding")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Bone Marrow Failure Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("May involve mutations in TERT or TERC genes.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Avoid crowded areas and monitor blood counts.")
        st.success("تجنب الزحام وراقب فحوصات الدم.")

    elif name == "Hereditary Blindness":
        st.header("Hereditary Blindness (العمى الوراثي)")
        st.subheader("Definition (تعريف):")
        st.write("Genetic disorders that cause progressive or congenital vision loss.")
        st.write("اضطرابات وراثية تسبب فقدان البصر التدريجي أو منذ الولادة.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Vision loss\n- Night blindness\n- Retinal degeneration")
        st.subheader("Causes (الأسباب):")
        st.write("Mutations in genes like RHO, RPGR, or CEP290.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Eye protection\n- Orientation support")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Genetic Sensory Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with mutations in multiple retinal genes.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Use vision aids and attend regular eye exams.")
        st.success("استخدم أدوات مساعدة وتابع طبيب العيون.")

    elif name == "Wilson's Disease":
        st.header("Wilson's Disease (مرض ويلسون)")
        st.subheader("Definition (تعريف):")
        st.write("A genetic disorder where excess copper builds up in the body.")
        st.write("اضطراب وراثي يتراكم فيه النحاس في الجسم.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Liver disease\n- Neurological symptoms\n- Personality changes")
        st.subheader("Causes (الأسباب):")
        st.write("Mutation in ATP7B gene causes copper accumulation.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Avoid copper-rich foods\n- Seek medical treatment")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Metabolic Genetic Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("ATP7B gene mutation on chromosome 13.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Low copper diet and medication help control symptoms.")
        st.success("اتبع نظامًا غذائيًا منخفض النحاس.")

    elif name == "Multiple Sclerosis":
        st.header("Multiple Sclerosis (التصلب المتعدد)")
        st.subheader("Definition (تعريف):")
        st.write("An autoimmune condition that affects the central nervous system.")
        st.write("حالة مناعية ذاتية تؤثر على الجهاز العصبي المركزي.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Numbness\n- Muscle weakness\n- Vision problems\n- Coordination issues")
        st.subheader("Causes (الأسباب):")
        st.write("Autoimmune attack on myelin sheath, possibly with genetic susceptibility.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Rest\n- Physical therapy\n- Seek neurological care")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Autoimmune Neurological Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with HLA-DRB1 gene.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Manage stress and follow treatment plan.")
        st.success("تجنب التوتر وواصل العلاج.")

    elif name == "Lupus (SLE)":
        st.header("Lupus (الذئبة الحمراء)")
        st.subheader("Definition (تعريف):")
        st.write("An autoimmune disease where the immune system attacks the body’s own tissues.")
        st.write("مرض مناعي ذاتي يهاجم فيه الجهاز المناعي أنسجة الجسم.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Joint pain\n- Fatigue\n- Skin rash\n- Organ inflammation")
        st.subheader("Causes (الأسباب):")
        st.write("Genetic and environmental factors trigger autoimmunity.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Avoid sun exposure\n- Manage pain")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Autoimmune Systemic Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with HLA-DR2 and DR3.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Use sun protection and anti-inflammatory medications.")
        st.success("احمِ نفسك من الشمس وتابع العلاج.")

    elif name == "Rheumatoid Arthritis":
        st.header("Rheumatoid Arthritis (الروماتويد)")
        st.subheader("Definition (تعريف):")
        st.write("An autoimmune disease causing inflammation in joints.")
        st.write("مرض مناعي ذاتي يسبب التهاب المفاصل.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Joint swelling\n- Pain\n- Morning stiffness\n- Fatigue")
        st.subheader("Causes (الأسباب):")
        st.write("Caused by immune system attacking joint tissue, linked to HLA genes.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Cold compresses\n- Pain relief\n- Medical attention")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Autoimmune Inflammatory Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with HLA-DR4 gene.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Exercise gently and take medications as prescribed.")
        st.success("مارس التمارين الخفيفة وتناول أدويتك بانتظام.")
    elif name == "High Blood Pressure":
        st.header("High Blood Pressure (الضغط العالي)")
        st.subheader("Definition (تعريف):")
        st.write("A chronic condition where the force of the blood against artery walls is too high.")
        st.write("حالة مزمنة يكون فيها ضغط الدم على جدران الشرايين مرتفعًا.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Often silent\n- Headaches\n- Dizziness\n- Vision problems")
        st.subheader("Causes (الأسباب):")
        st.write("Genetics, lifestyle, stress, and kidney disease.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Rest\n- Lower salt intake\n- Emergency care if very high")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Chronic Cardiovascular Condition")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to genes such as AGT, ACE.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Monitor your blood pressure regularly.")
        st.success("راقب ضغط دمك بانتظام.")

    elif name == "Asthma":
        st.header("Asthma (الربو)")
        st.subheader("Definition (تعريف):")
        st.write("A condition in which airways narrow and swell, producing extra mucus.")
        st.write("حالة تضيق فيها الممرات الهوائية وتنتفخ وتنتج مخاطًا زائدًا.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Shortness of breath\n- Wheezing\n- Coughing")
        st.subheader("Causes (الأسباب):")
        st.write("Genetic and environmental factors, allergens, and pollution.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Use inhaler\n- Move to fresh air\n- Seek emergency help")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Chronic Respiratory Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with ORMDL3 gene and others.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Avoid triggers and carry your inhaler.")
        st.success("تجنب المثيرات واحمل بخاخك دائماً.")

    elif name == "Type 2 Diabetes":
        st.header("Type 2 Diabetes (السكري النوع ٢)")
        st.subheader("Definition (تعريف):")
        st.write("A chronic condition that affects the way the body processes blood sugar.")
        st.write("حالة مزمنة تؤثر على طريقة معالجة الجسم لسكر الدم.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Increased thirst\n- Frequent urination\n- Fatigue\n- Blurred vision")
        st.subheader("Causes (الأسباب):")
        st.write("Genetics, obesity, inactivity, and insulin resistance.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Check blood sugar\n- Provide sugar for hypoglycemia\n- Emergency care if needed")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Metabolic Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to TCF7L2, PPARG genes.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Maintain a healthy lifestyle and monitor glucose.")
        st.success("حافظ على نمط حياة صحي وراقب السكر.")

    elif name == "Autism":
        st.header("Autism (التوحد)")
        st.subheader("Definition (تعريف):")
        st.write("A developmental disorder affecting communication and behavior.")
        st.write("اضطراب نمائي يؤثر على التواصل والسلوك.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Social difficulties\n- Repetitive behaviors\n- Delayed speech")
        st.subheader("Causes (الأسباب):")
        st.write("Complex interplay of genetic and environmental factors.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Provide calm environment\n- Support routines")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Neurodevelopmental Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to SHANK3, MECP2, and others.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Early therapy and supportive care are crucial.")
        st.success("التدخل المبكر والرعاية مهمان جداً.")

    elif name == "Schizophrenia":
        st.header("Schizophrenia (الشيزوفرينيا)")
        st.subheader("Definition (تعريف):")
        st.write("A serious mental disorder that affects how a person thinks, feels, and behaves.")
        st.write("اضطراب نفسي خطير يؤثر على التفكير والمشاعر والسلوك.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Delusions\n- Hallucinations\n- Disorganized thinking")
        st.subheader("Causes (الأسباب):")
        st.write("Genetics, brain chemistry, environmental factors.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Keep the person safe\n- Call for psychiatric help")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Mental Psychiatric Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to DISC1, COMT, and others.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Continuous psychiatric support is essential.")
        st.success("الدعم النفسي المستمر ضروري.")

    elif name == "Breast Cancer":
        st.header("Breast Cancer (سرطان الثدي)")
        st.subheader("Definition (تعريف):")
        st.write("A disease where cells in the breast grow out of control.")
        st.write("مرض تنمو فيه خلايا الثدي بشكل غير طبيعي.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Lump in the breast\n- Change in breast shape\n- Nipple discharge")
        st.subheader("Causes (الأسباب):")
        st.write("Genetic mutations (BRCA1/2), age, hormones, lifestyle.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Seek immediate medical evaluation")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Cancerous Tumor Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to BRCA1, BRCA2 genes.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Do regular self-exams and screenings.")
        st.success("افحصي نفسك بانتظام وقومي بالكشف الدوري.")

    elif name == "Alzheimer's Disease":
        st.header("Alzheimer's Disease (الزهايمر)")
        st.subheader("Definition (تعريف):")
        st.write("A progressive brain disorder that slowly destroys memory and thinking skills.")
        st.write("اضطراب دماغي تدريجي يدمر الذاكرة ومهارات التفكير.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Memory loss\n- Confusion\n- Personality changes")
        st.subheader("Causes (الأسباب):")
        st.write("Combination of genetic, environmental, and lifestyle factors.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Keep environment familiar\n- Provide reminders and safety")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Neurodegenerative Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to APOE-e4, APP, PSEN1/2.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Maintain routine and engage in mental activities.")
        st.success("احفظ الروتين وقم بأنشطة ذهنية.")

    elif name == "ALS":
        st.header("ALS (التصلب الجانبي الضموري)")
        st.subheader("Definition (تعريف):")
        st.write("A progressive neurodegenerative disease affecting nerve cells in the brain and spinal cord.")
        st.write("مرض عصبي تنكسي تدريجي يؤثر على الخلايا العصبية في الدماغ والنخاع الشوكي.")
        st.subheader("Symptoms (الأعراض):")
        st.write("- Muscle weakness\n- Difficulty speaking/swallowing\n- Paralysis")
        st.subheader("Causes (الأسباب):")
        st.write("Some cases are genetic, linked to mutations in SOD1, C9orf72.")
        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("- Respiratory support\n- Assistive devices")
        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Neurodegenerative Genetic Disorder")
        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to SOD1, FUS, C9orf72 genes.")
        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Supportive care and therapy can improve quality of life.")
        st.success("الرعاية المساندة والعلاج تحسن جودة الحياة.")
