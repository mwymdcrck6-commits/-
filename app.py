import streamlit as st
import random
from typing import List, Dict

# ==================== ПОЛНЫЙ ПЛАН СЧЁТОВ ====================
ACCOUNTS: List[Dict] = [
    {"number": "01", "name": "Основные средства", "type": "А", "section": "Внеоборотные активы"},
    {"number": "02", "name": "Амортизация основных средств", "type": "П", "section": "Внеоборотные активы"},
    {"number": "03", "name": "Доходные вложения в материальные ценности", "type": "А", "section": "Внеоборотные активы"},
    {"number": "04", "name": "Нематериальные активы", "type": "А", "section": "Внеоборотные активы"},
    {"number": "05", "name": "Амортизация нематериальных активов", "type": "П", "section": "Внеоборотные активы"},
    {"number": "07", "name": "Оборудование к установке", "type": "А", "section": "Внеоборотные активы"},
    {"number": "08", "name": "Вложения во внеоборотные активы", "type": "А", "section": "Внеоборотные активы"},
    {"number": "09", "name": "Отложенные налоговые активы", "type": "А", "section": "Внеоборотные активы"},
    {"number": "10", "name": "Материалы", "type": "А", "section": "Производственные запасы"},
    {"number": "11", "name": "Животные на выращивании и откорме", "type": "А", "section": "Производственные запасы"},
    {"number": "14", "name": "Резервы под снижение стоимости материальных ценностей", "type": "П", "section": "Производственные запасы"},
    {"number": "20", "name": "Основное производство", "type": "А", "section": "Затраты на производство"},
    {"number": "90", "name": "Продажи", "type": "АП", "section": "Финансовые результаты"}
    # Список можно дополнить другими счетами
]

def main():
    st.set_page_config(
        page_title="План счетов — Тест",
        page_icon="🧾",
        layout="centered",  # Адаптация макета под мобильное устройство
        initial_sidebar_state="collapsed"
    )

    st.title("🧾 Тест: План счетов")  # Укороченное название для компактности
    st.caption("Приказ Минфина РФ № 94н • Полный список счетов")

    tab1, tab2 = st.tabs(["🧪 Тест", "📖 Справочник"])

    with tab1:
        with st.sidebar:
            st.header("Настройки теста")
            mode = st.radio("Тип вопросов", ["Ввод номера", "Выбор варианта"])
            num_questions = st.slider("Вопросы", 5, 20, 10)  # Ограничить максимум до 20
            test_mode = st.radio("Раздел", ["Все счета", "По разделу"])
            
            if test_mode == "По разделу":
                sections = sorted(list(set(a["section"] for a in ACCOUNTS)))
                selected_section = st.selectbox("Раздел", sections)
            else:
                selected_section = None

            if st.button("🚀 Начать"):
                st.session_state.test_started = True
                st.session_state.current = 0
                st.session_state.score = 0
                st.session_state.questions = []

                if test_mode == "По разделу" and selected_section:
                    filtered = [acc for acc in ACCOUNTS if acc["section"] == selected_section]
                else:
                    filtered = ACCOUNTS.copy()

                st.session_state.questions = random.sample(filtered, min(num_questions, len(filtered)))
                st.rerun()

        if st.session_state.get('test_started', False) and 'questions' in st.session_state:
            if st.session_state.current < len(st.session_state.questions):
                q = st.session_state.questions[st.session_state.current]
                
                st.progress(st.session_state.current / len(st.session_state.questions))
                st.subheader(f"Вопрос {st.session_state.current + 1} из {len(st.session_state.questions)}")
                st.info(f"**{q['name']}**")

                if mode == "Ввод номера":
                    user_answer = st.text_input("Введите номер", placeholder="51")
                    if st.button("Проверить"):
                        correct = q["number"]
                        if user_answer.strip() == correct:
                            st.success(f"✅ Верно! Счёт **{correct}**")
                            st.session_state.score += 1
                        else:
                            st.error(f"❌ Ошибка. Ответ: **{correct}**")
                        st.session_state.current += 1
                        st.rerun()
                else:
                    options = [q["number"]]
                    while len(options) < 4:
                        wrong = random.choice(ACCOUNTS)["number"]
                        if wrong not in options:
                            options.append(wrong)
                    random.shuffle(options)
                    
                    answers_map = {opt: opt == q["number"] for opt in options}  # Карта ответов для точной проверки
                    for opt in options:
                        if st.button(opt):
                            if answers_map[opt]:
                                st.success("✅ Верно!")
                                st.session_state.score += 1
                            else:
                                st.error(f"❌ Ошибка: **{q['number']}**")
                            st.session_state.current += 1
                            st.rerun()
            else:
                st.success(f"🎉 Тест завершён! Ваш результат: {st.session_state.score} из {len(st.session_state.questions)}")
                # Сохранить состояние для нового теста
                if st.button("🔄 Новый тест"):
                    st.session_state.test_started = False
                    st.rerun()
        else:
            st.info("👈 Выберите настройки слева")

    with tab2:
        st.subheader("📖 Справочник")
        search = st.text_input("🔍 Поиск")
        filtered_accounts = ACCOUNTS
        if search:
            filtered_accounts = [a for a in ACCOUNTS if search.lower() in a["number"].lower() or search.lower() in a["name"].lower()]
        
        for acc in filtered_accounts[:10]:  # Ограничение на вывод 10 элементов
            st.write(f"**{acc['number']}** — {acc['name']} ({acc['type']}) • {acc['section']}")

if __name__ == "__main__":
    main()