"""
Treatment recommendation service for rice diseases
"""
import streamlit as st
from typing import Dict, Any

class TreatmentService:
    """Service class for providing treatment recommendations"""
    
    def __init__(self):
        self.treatments = self._load_treatments()
    
    def _load_treatments(self) -> Dict[str, Dict[str, Any]]:
        """Load treatment recommendations for different diseases"""
        return {
            'Neck_Blast': {
                'title': '🌾 Neck Blast (গোড়ার দাগ রোগ)',
                'cause': 'এটি *Magnaporthe oryzae* ছত্রাক দ্বারা সৃষ্টি হয়। ফুল আসার সময় ছত্রাক গোঁড়া আক্রমণ করে ধান ঝরে যায়।',
                'symptoms': [
                    'গাছের কাণ্ডের ঠিক নিচে বাদামী বা ধূসর রঙের দাগ দেখা যায়।',
                    'আক্রান্ত কন্ঠী শুকিয়ে যায় ও দানা তৈরি হয় না।',
                    'রোগ বেশি হলে ফলনের ক্ষতি ৮০% পর্যন্ত হতে পারে।'
                ],
                'biological_control': [
                    'রোগমুক্ত বীজ ব্যবহার করুন।',
                    'ধান রোপণের পূর্বে বীজ গরম পানিতে শোধন করুন।',
                    'জমিতে পর্যাপ্ত পানি নিষ্কাশনের ব্যবস্থা রাখুন।'
                ],
                'chemical_control': [
                    'ট্রাইসাইক্লাজল (Tricyclazole) বা আজোক্সিস্ট্রোবিন (Azoxystrobin) স্প্রে করুন।',
                    'ফুল আসার সময় ও ৭ দিন পর দ্বিতীয় স্প্রে করুন।'
                ]
            },
            'Leaf scald': {
                'title': '🌾 Leaf Scald (পাতা পুড়ে যাওয়া রোগ)',
                'cause': '*Microdochium oryzae* নামক ছত্রাকের মাধ্যমে ছড়ায়।',
                'symptoms': [
                    'পাতার কিনারায় হালকা বাদামী দাগ যা পরে গাঢ় বাদামী হয়।',
                    'পাতার উপরিভাগে আগুনে পোড়ার মতো দাগ পড়ে।'
                ],
                'biological_control': [
                    'রোগমুক্ত চারা রোপণ করুন।',
                    'জমিতে অতিরিক্ত নাইট্রোজেন ব্যবহার এড়িয়ে চলুন।',
                    'পর্যাপ্ত রোদ ও বাতাস নিশ্চিত করুন।'
                ],
                'chemical_control': [
                    'প্রয়োজনে ট্রাইসাইক্লাজল জাতীয় ছত্রাকনাশক প্রয়োগ করুন।'
                ]
            },
            'Sheath Blight': {
                'title': '🌾 Sheath Blight (পাতার গোড়া পচা রোগ)',
                'cause': '*Rhizoctonia solani* ছত্রাকের আক্রমণে হয়।',
                'symptoms': [
                    'পাতার গোড়ায় বাদামী বা ছাই রঙের দাগ দেখা যায়।',
                    'দাগগুলো ধীরে ধীরে বড় হয়ে পুরো পাতাকে মেরে ফেলে।'
                ],
                'biological_control': [
                    'সারির ব্যবধান রেখে রোপণ করুন।',
                    'রোগমুক্ত জমিতে চাষ করুন।'
                ],
                'chemical_control': [
                    'হেক্সাকোনাজল বা ভ্যালিডামাইসিন জাতীয় ছত্রাকনাশক ব্যবহার করুন।',
                    'স্প্রে ২ বার করুন – শুরুর লক্ষণ দেখা গেলে এবং ৭ দিন পরে।'
                ]
            },
            'Healthy Rice Leaf': {
                'title': '🌾 Healthy Rice Leaf (সুস্থ ধানের পাতা)',
                'cause': 'সুস্থ অবস্থা',
                'symptoms': [
                    'পাতায় কোনো দাগ বা বিবর্ণতা নেই।',
                    'পাতার রং গাঢ় সবুজ ও শক্তিশালী।'
                ],
                'biological_control': [
                    'এ অবস্থায় কোনো নিয়ন্ত্রণের প্রয়োজন নেই, বরং সুস্থ অবস্থাকে বজায় রাখার জন্য নিয়মিত পর্যবেক্ষণ জরুরি।'
                ],
                'chemical_control': []
            },
            'Narrow Brown Leaf Spot': {
                'title': '🌾 Narrow Brown Leaf Spot (পাতায় সরু বাদামী দাগ)',
                'cause': '*Septoria oryzae* ছত্রাকজনিত রোগ।',
                'symptoms': [
                    'পাতায় সরু লম্বা বাদামী দাগ দেখা যায়।',
                    'দাগগুলো একত্রে হয়ে পাতা শুকিয়ে ফেলতে পারে।'
                ],
                'biological_control': [
                    'রোগমুক্ত বীজ ব্যবহার করুন।',
                    'সুষম সার ব্যবহার করুন।'
                ],
                'chemical_control': [
                    'প্রয়োজনে কপার ভিত্তিক ছত্রাকনাশক প্রয়োগ করা যেতে পারে।'
                ]
            },
            'Leaf Blast': {
                'title': '🌾 Leaf Blast (পাতায় দাগ রোগ)',
                'cause': '*Magnaporthe oryzae* ছত্রাকের মাধ্যমে ছড়ায়।',
                'symptoms': [
                    'পাতায় ডায়মন্ড আকৃতির ছাই বা বাদামী দাগ দেখা যায়।',
                    'দাগ বড় হয়ে পাতাকে মেরে ফেলে।'
                ],
                'biological_control': [
                    'রোগমুক্ত বীজ ব্যবহার করুন।',
                    'ধান ঘনভাবে রোপণ এড়িয়ে চলুন।'
                ],
                'chemical_control': [
                    'ট্রাইসাইক্লাজল স্প্রে করুন।'
                ]
            },
            'Rice Hispa': {
                'title': '🌾 Rice Hispa (রাইস হিছপা কীট আক্রমণ)',
                'cause': '*Dicladispa armigera* নামক পোকা দ্বারা আক্রান্ত হয়।',
                'symptoms': [
                    'পাতার উপরিভাগে আঁকাবাঁকা সাদা দাগ পড়ে।',
                    'পোকা পাতার সবুজ অংশ খেয়ে ফেলে।'
                ],
                'biological_control': [
                    'আক্রান্ত পাতা তুলে ফেলুন।',
                    'শিকারি পোকা সংরক্ষণ করুন।'
                ],
                'chemical_control': [
                    'ইমিডাক্লোপরিড বা কুইনালফস স্প্রে করা যেতে পারে।'
                ]
            },
            'Brown Spot': {
                'title': '🌾 Brown Spot (পাতায় বাদামী দাগ রোগ)',
                'cause': '*Bipolaris oryzae* ছত্রাক দ্বারা সৃষ্ট।',
                'symptoms': [
                    'পাতায় গোল বাদামী দাগ দেখা যায়।',
                    'দাগের কেন্দ্রে সাদা এবং চারপাশে গাঢ় বাদামী।'
                ],
                'biological_control': [
                    'ভালো নিষ্কাশন ব্যবস্থা নিশ্চিত করুন।',
                    'সুষম সার ব্যবহার করুন।'
                ],
                'chemical_control': [
                    'ম্যানকোজেব জাতীয় ছত্রাকনাশক প্রয়োগ করুন।'
                ]
            },
            'Bacterial Leaf Blight': {
                'title': '🌾 Bacterial Leaf Blight (পাতা পঁচা ব্যাকটেরিয়া রোগ)',
                'cause': '*Xanthomonas oryzae pv. oryzae* ব্যাকটেরিয়া দ্বারা হয়।',
                'symptoms': [
                    'পাতার কিনারা থেকে দাগ শুরু হয়ে পুরো পাতা শুকিয়ে ফেলে।',
                    'সকালে পাতায় হালকা সাদা আঠালো তরল দেখা যায়।'
                ],
                'biological_control': [
                    'রোগমুক্ত বীজ ব্যবহার করুন।',
                    'জমিতে পানি জমতে দেবেন না।'
                ],
                'chemical_control': [
                    'কপার অক্সিক্লোরাইড বা স্ট্রেপ্টোসাইক্লিন প্রয়োগ করা যেতে পারে।'
                ]
            }
        }
    
    def get_treatment(self, disease_name: str) -> str:
        """Get treatment recommendation for a specific disease"""
        if disease_name not in self.treatments:
            return "Unknown disease. Please consult with an agricultural expert."
        
        treatment = self.treatments[disease_name]
        
        # Format the treatment information
        markdown = f"""
        ### {treatment['title']}

        **🦠 কারণ:**  
        {treatment['cause']}

        **🔍 লক্ষণ:**  
        """
        
        for symptom in treatment['symptoms']:
            markdown += f"- {symptom}  \n"
        
        if treatment['biological_control']:
            markdown += "\n#### 🌱 জৈবিক নিয়ন্ত্রণ:  \n"
            for control in treatment['biological_control']:
                markdown += f"- {control}  \n"
        
        if treatment['chemical_control']:
            markdown += "\n#### 💊 রাসায়নিক নিয়ন্ত্রণ:  \n"
            for control in treatment['chemical_control']:
                markdown += f"- {control}  \n"
        
        return markdown
    
    def display_treatment(self, disease_name: str):
        """Display treatment recommendation in Streamlit"""
        treatment_markdown = self.get_treatment(disease_name)
        st.markdown(treatment_markdown)
