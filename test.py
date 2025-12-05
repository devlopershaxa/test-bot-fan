import telebot
from telebot import types
import random

# Bot tokenini shu yerga qo'ying
TOKEN = '8538799525:AAFgBkZNwE4n_BLA5UXOteYlMGhm52nKVMU'
bot = telebot.TeleBot(TOKEN)

# Fanlar bo'yicha test savollari
questions = {
    "matematika": [
        {
            "question": "1. 25 + 37 = ?",
            "options": ["52", "62", "72", "61"],
            "correct": 1
        },
        {
            "question": "2. 48 - 19 = ?",
            "options": ["29", "39", "28", "31"],
            "correct": 0
        },
        {
            "question": "3. 6 × 7 = ?",
            "options": ["42", "36", "48", "49"],
            "correct": 0
        },
        {
            "question": "4. 81 ÷ 9 = ?",
            "options": ["7", "8", "9", "10"],
            "correct": 2
        },
        {
            "question": "5. Kvadratning perimetri qanday hisoblanadi?",
            "options": ["a×b", "a+b+c+d", "4×a", "2×(a+b)"],
            "correct": 2
        },
        {
            "question": "6. 3² = ?",
            "options": ["6", "9", "8", "5"],
            "correct": 1
        },
        {
            "question": "7. 1 soat necha minut?",
            "options": ["30", "60", "90", "100"],
            "correct": 1
        },
        {
            "question": "8. Eng katta bir xonali son?",
            "options": ["8", "9", "10", "11"],
            "correct": 1
        },
        {
            "question": "9. 1 km necha metr?",
            "options": ["10", "100", "1000", "10000"],
            "correct": 2
        },
        {
            "question": "10. Tenglamani yeching: x + 5 = 12",
            "options": ["6", "7", "8", "9"],
            "correct": 1
        },
        {
            "question": "11. 3 dan 5 ta ortiq son?",
            "options": ["7", "8", "9", "10"],
            "correct": 1
        },
        {
            "question": "12. To'g'ri to'rtburchakning yuzi qanday hisoblanadi?",
            "options": ["a+b", "a×b", "2×(a+b)", "4×a"],
            "correct": 1
        },
        {
            "question": "13. 1 tonna necha kilogramm?",
            "options": ["10", "100", "1000", "10000"],
            "correct": 2
        },
        {
            "question": "14. 1 hafta necha kun?",
            "options": ["5", "6", "7", "8"],
            "correct": 2
        },
        {
            "question": "15. 2³ = ?",
            "options": ["6", "8", "9", "4"],
            "correct": 1
        }
    ],
    "ona_tili": [
        {
            "question": "1. Qaysi so'zda norasmiy ulanish bor?",
            "options": ["uyga", "keldim", "kitobni", "stolda"],
            "correct": 1
        },
        {
            "question": "2. Qaysi gapda fe'l qatnashmagan?",
            "options": ["Qalam yo'q", "Men kitob o'qiyman", "U uyga ketdi", "Bolalar maktabga bordi"],
            "correct": 0
        },
        {
            "question": "3. Qaysi so'zda unlilar qo'shimchasi bor?",
            "options": ["maktab", "darslik", "kitob", "sinfdosh"],
            "correct": 3
        },
        {
            "question": "4. Qaysi gapda sifat qatnashgan?",
            "options": ["Chiroyli gul", "Yoz keldi", "U bola", "Maktabga bordik"],
            "correct": 0
        },
        {
            "question": "5. Qaysi so'zda qatnashuvchi tovushlar mavjud?",
            "options": ["soat", "ko'cha", "daraxt", "bolalar"],
            "correct": 1
        },
        {
            "question": "6. Antonim so'zlarni toping",
            "options": ["katta-kichik", "chiroyli-gul", "kitob-darslik", "maktab-sinf"],
            "correct": 0
        },
        {
            "question": "7. Sinonim so'zlarni toping",
            "options": ["kel-di", "chiroyli-gul", "yaxshi-chirayli", "maktab-sinf"],
            "correct": 2
        },
        {
            "question": "8. Qaysi so'zda qo'shimcha undosh bor?",
            "options": ["kitob", "maktab", "gul", "daraxt"],
            "correct": 1
        },
        {
            "question": "9. Qaysi gapda aniqlovchi qatnashgan?",
            "options": ["Yashil daraxt", "U bola", "Maktabga bordik", "Qalam yo'q"],
            "correct": 0
        },
        {
            "question": "10. Qaysi so'zda undoshlar qo'shimchasi bor?",
            "options": ["bolalar", "gul", "kitob", "maktab"],
            "correct": 0
        },
        {
            "question": "11. Qaysi gapda ravish qatnashgan?",
            "options": ["Juda chiroyli", "Yaxshi bola", "Tez yugurdi", "Kitob o'qidi"],
            "correct": 2
        },
        {
            "question": "12. Qaysi so'zda unlilar qo'shimchasi yo'q?",
            "options": ["maktab", "sinfdosh", "kitob", "gul"],
            "correct": 3
        },
        {
            "question": "13. Qaysi gapda egalik munosabati ifodalanmagan?",
            "options": ["Mening kitobim", "Uning daftari", "Sinf xonalari", "Bolalar"],
            "correct": 3
        },
        {
            "question": "14. Qaysi so'zda qo'shimcha undoshlar bor?",
            "options": ["sinfdosh", "maktab", "kitob", "gul"],
            "correct": 0
        },
        {
            "question": "15. Qaysi gapda kesim qatnashmagan?",
            "options": ["Men kitob o'qiyman", "U bola", "Maktabga bordik", "Qalam yo'q"],
            "correct": 3
        }
    ],
    "ingliz_tili": [
        {
            "question": "1. What is the opposite of 'big'?",
            "options": ["small", "large", "huge", "great"],
            "correct": 0
        },
        {
            "question": "2. Choose the correct verb: She _____ to school every day.",
            "options": ["go", "goes", "going", "gone"],
            "correct": 1
        },
        {
            "question": "3. How do you say 'kitob' in English?",
            "options": ["pen", "book", "pencil", "bag"],
            "correct": 1
        },
        {
            "question": "4. What is the plural of 'child'?",
            "options": ["childs", "children", "childes", "childies"],
            "correct": 1
        },
        {
            "question": "5. Choose the correct translation: Men maktabga boraman",
            "options": ["I go to school", "I goes to school", "I am go to school", "I going to school"],
            "correct": 0
        },
        {
            "question": "6. Which word means 'rang'?",
            "options": ["red", "color", "blue", "green"],
            "correct": 1
        },
        {
            "question": "7. What comes after Tuesday?",
            "options": ["Monday", "Wednesday", "Thursday", "Friday"],
            "correct": 1
        },
        {
            "question": "8. Choose the correct spelling:",
            "options": ["beutiful", "beautiful", "butiful", "beatiful"],
            "correct": 1
        },
        {
            "question": "9. How many vowels are there in English?",
            "options": ["3", "4", "5", "6"],
            "correct": 2
        },
        {
            "question": "10. What is the past tense of 'go'?",
            "options": ["goed", "went", "goes", "going"],
            "correct": 1
        },
        {
            "question": "11. Choose the correct article: I have ___ apple.",
            "options": ["a", "an", "the", "some"],
            "correct": 1
        },
        {
            "question": "12. Which word is a number?",
            "options": ["cat", "dog", "three", "book"],
            "correct": 2
        },
        {
            "question": "13. What is the opposite of 'hot'?",
            "options": ["warm", "cool", "cold", "chilly"],
            "correct": 2
        },
        {
            "question": "14. How do you say 'kompyuter' in English?",
            "options": ["computer", "television", "radio", "phone"],
            "correct": 0
        },
        {
            "question": "15. Choose the correct sentence:",
            "options": ["She is a teacher", "She are a teacher", "She am a teacher", "She be a teacher"],
            "correct": 0
        }
    ]
}

# Foydalanuvchi holati
user_states = {}

# Test natijalari
user_results = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    
    # Foydalanuvchi ma'lumotlarini boshlang'ich qiymatlarga o'rnatish
    user_states[chat_id] = {
        'subject': None,
        'current_question': 0,
        'score': 0,
        'answers': []
    }
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Matematika")
    btn2 = types.KeyboardButton("Ona tili")
    btn3 = types.KeyboardButton("Ingliz tili")
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(chat_id, "Salom! 5-sinf fanlari bo'yicha test botiga xush kelibsiz!\nQaysi fandan test o'tmoqchisiz?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Matematika", "Ona tili", "Ingliz tili"])
def select_subject(message):
    chat_id = message.chat.id
    subject_map = {
        "Matematika": "matematika",
        "Ona tili": "ona_tili",
        "Ingliz tili": "ingliz_tili"
    }
    
    user_states[chat_id]['subject'] = subject_map[message.text]
    user_states[chat_id]['current_question'] = 0
    user_states[chat_id]['score'] = 0
    user_states[chat_id]['answers'] = []
    
    send_question(chat_id)

def send_question(chat_id):
    user_state = user_states.get(chat_id)
    if not user_state:
        return
        
    subject = user_state['subject']
    question_index = user_state['current_question']
    
    # Agar barcha savollar tugagan bo'lsa, natijani ko'rsatish
    if question_index >= len(questions[subject]):
        show_results(chat_id)
        return
    
    question_data = questions[subject][question_index]
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i, option in enumerate(question_data['options']):
        markup.add(types.KeyboardButton(f"{chr(65+i)}) {option}"))
    
    bot.send_message(chat_id, question_data['question'], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.startswith(tuple([f"{chr(65+i)})" for i in range(4)])))
def handle_answer(message):
    chat_id = message.chat.id
    user_state = user_states.get(chat_id)
    
    if not user_state or user_state['subject'] is None:
        bot.send_message(chat_id, "Iltimos, avval fanni tanlang /start tugmasini bosing")
        return
    
    subject = user_state['subject']
    question_index = user_state['current_question']
    
    # Javobni aniqlash
    answer_letter = message.text[0]  # A, B, C yoki D
    answer_index = ord(answer_letter) - 65  # A=0, B=1, C=2, D=3
    
    # To'g'ri javobni tekshirish
    correct_index = questions[subject][question_index]['correct']
    is_correct = answer_index == correct_index
    
    # Natijalarni saqlash
    user_state['answers'].append({
        'question': question_index,
        'answer': answer_index,
        'correct': is_correct
    })
    
    if is_correct:
        user_state['score'] += 1
    
    # Keyingi savolga o'tish
    user_state['current_question'] += 1
    
    # Keyingi savolni yuborish
    send_question(chat_id)

def show_results(chat_id):
    user_state = user_states.get(chat_id)
    if not user_state:
        return
        
    subject = user_state['subject']
    score = user_state['score']
    total = len(questions[subject])
    
    # Natijani hisoblash
    percentage = (score / total) * 100
    
    # Bahoni aniqlash
    if percentage >= 90:
        grade = "A'lo (5 ball)"
    elif percentage >= 75:
        grade = "Yaxshi (4 ball)"
    elif percentage >= 60:
        grade = "Qoniqarli (3 ball)"
    else:
        grade = "Qoniqarsiz (2 ball)"
    
    # Xabar tayyorlash
    result_msg = f"Test yakunlandi!\n\n"
    result_msg += f"To'g'ri javoblar: {score}/{total}\n"
    result_msg += f"Foiz: {percentage:.1f}%\n"
    result_msg += f"Baho: {grade}\n\n"
    
    if score == total:
        result_msg += "Tabriklaymiz! Siz barcha savollarga to'g'ri javob berdingiz!"
    elif score >= total * 0.8:
        result_msg += "Yaxshi natija! Ozgina mashq qilsangiz hammasi joyida bo'ladi."
    elif score >= total * 0.6:
        result_msg += "Yana biroz harakat qilsangiz yaxshi natija qo'lga kiritasiz."
    else:
        result_msg += "Ko'proq o'qish va mashq qilish kerak."
    
    # Yangi test boshlash tugmasini qo'shish
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("/start")
    markup.add(btn)
    
    bot.send_message(chat_id, result_msg, reply_markup=markup)

# Botni ishga tushirish
if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.polling(none_stop=True)