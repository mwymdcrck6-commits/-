import streamlit as st
import random
from typing import List, Dict

# Данные по плану счетов
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
    {"number": "15", "name": "Заготовление и приобретение материальных ценностей", "type": "А", "section": "Производственные запасы"},
    {"number": "16", "name": "Отклонение в стоимости материальных ценностей", "type": "АП", "section": "Производственные запасы"},
    
    {"number": "19", "name": "Налог на добавленную стоимость по приобретенным ценностям", "type": "А", "section": "НДС"},
    
    {"number": "20", "name": "Основное производство", "type": "А", "section": "Затраты на производство"},
    {"number": "21", "name": "Полуфабрикаты собственного производства", "type": "А", "section": "Затраты на производство"},
    {"number": "23", "name": "Вспомогательные производства", "type": "А", "section": "Затраты на производство"},
    {"number": "25", "name": "Общепроизводственные расходы", "type": "А", "section": "Затраты на производство"},
    {"number": "26", "name": "Общехозяйственные расходы", "type": "А", "section": "Затраты на производство"},
    {"number": "28", "name": "Брак в производстве", "type": "А", "section": "Затраты на производство"},
    {"number": "29", "name": "Обслуживающие производства и хозяйства", "type": "А", "section": "Затраты на производство"},
    
    {"number": "40", "name": "Выпуск продукции (работ, услуг)", "type": "АП", "section": "Готовая продукция"},
    {"number": "41", "name": "Товары", "type": "А", "section": "Готовая продукция"},
    {"number": "43", "name": "Готовая продукция", "type": "А", "section": "Готовая продукция"},
    {"number": "44", "name": "Расходы на продажу", "type": "А", "section": "Готовая продукция"},
    {"number": "45", "name": "Товары отгруженные", "type": "А", "section": "Готовая продукция"},
    
    {"number": "50", "name": "Касса", "type": "А", "section": "Денежные средства"},
    {"number": "51", "name": "Расчетные счета", "type": "А", "section": "Денежные средства"},
    {"number": "52", "name": "Валютные счета", "type": "А", "section": "Денежные средства"},
    {"number": "55", "name": "Специальные счета в банках", "type": "А", "section": "Денежные средства"},
    {"number": "57", "name": "Переводы в пути", "type": "А", "section": "Денежные средства"},
    {"number": "58", "name": "Финансовые вложения", "type": "А", "section": "Денежные средства"},
    {"number": "59", "name": "Резервы под обесценение финансовых вложений", "type": "П", "section": "Денежные средства"},
    
    {"number": "60", "name": "Расчеты с поставщиками и подрядчиками", "type": "АП", "section": "Расчеты"},
    {"number": "62", "name": "Расчеты с покупателями и заказчиками", "type": "АП", "section": "Расчеты"},
    {"number": "63", "name": "Резервы по сомнительным долгам", "type": "П", "section": "Расчеты"},
    {"number": "66", "name": "Расчеты по краткосрочным кредитам и займам", "type": "П", "section": "Расчеты"},
    {"number": "67", "name": "Расчеты по долгосрочным кредитам и займам", "type": "П", "section": "Расчеты"},
    {"number": "68", "name": "Расчеты по налогам и сборам", "type": "АП", "section": "Расчеты"},
    {"number": "69", "name": "Расчеты по социальному страхованию и обеспечению", "type": "АП", "section": "Расчеты"},
    {"number": "70", "name": "Расчеты с персоналом по оплате труда", "type": "П", "section": "Расчеты"},
    {"number": "71", "name": "Расчеты с подотчетными лицами", "type": "АП", "section": "Расчеты"},
    {"number": "73", "name": "Расчеты с персоналом по прочим операциям", "type": "АП", "section": "Расчеты"},
    {"number": "75", "name": "Расчеты с учредителями", "type": "АП", "section": "Расчеты"},
    {"number": "76", "name": "Расчеты с разными дебиторами и кредиторами", "type": "АП", "section": "Расчеты"},
    {"number": "77", "name": "Отложенные налоговые обязательства", "type": "П", "section": "Расчеты"},
    {"number": "79", "name": "Внутрихозяйственные расчеты", "type": "АП", "section": "Расчеты"},
    
    {"number": "80", "name": "Уставный капитал", "type": "П", "section": "Капитал"},
    {"number": "81", "name": "Собственные акции (доли)", "type": "А", "section": "Капитал"},
    {"number": "82", "name": "Резервный капитал", "type": "П", "section": "Капитал"},
    {"number": "83", "name": "Добавочный капитал", "type": "П", "section": "Капитал"},
    {"number": "84", "name": "Нераспределенная прибыль (непокрытый убыток)", "type": "АП", "section": "Капитал"},
    {"number": "86", "name": "Целевое финансирование", "type": "П", "section": "Капитал"},
    
    {"number": "90", "name": "Продажи", "type": "АП", "section": "Финансовые результаты"},
    {"number": "91", "name": "Прочие доходы и расходы", "type": "АП", "section": "Финансовые результаты"},
    {"number": "94", "name": "Недостачи и потери от порчи ценностей", "type": "А", "section": "Финансовые результаты"},
    {"number": "96", "name": "Резервы предстоящих расходов", "type": "П", "section": "Финансовые результаты"},
    {"number": "97", "name": "Расходы будущих периодов", "type": "А", "section": "Финансовые результаты"},
    {"number": "98", "name": "Доходы будущих периодов", "type": "П", "section": "Финансовые результаты"},
    {"number": "99", "name": "Прибыли и убытки", "type": "АП", "section": "Финансовые результаты"},
]

def main():
    st.set_page_config(page_title="Тест по Плану счетов", layout="centered")
    st.title("🧾 Тестирование знаний по Плану счетов бухгалтерского учёта")
    st.markdown("**Приказ Минфина РФ № 94н**")

    with st.sidebar:
        st.header("Настройки теста")
        mode = st.radio("Режим", ["Случайные вопросы", "По разделу"])
        num_questions = st.slider("Количество вопросов", 5, 30, 10, 5)
        
        if mode == "По разделу":
            sections = sorted(list(set(acc["section"] for acc in ACCOUNTS)))
            selected_section = st.selectbox("Выберите раздел", sections)
        else:
            selected_section = None

        if st.button("Начать тест", type="primary"):
            st.session_state.test_started = True
            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.answers = []
            
            if mode == "По разделу" and selected_section:
                filtered = [acc for acc in ACCOUNTS if acc["section"] == selected_section]
            else:
                filtered = ACCOUNTS.copy()
            
            st.session_state.questions = random.sample(filtered, min(num_questions, len(filtered)))

    if 'test_started' not in st.session_state:
        st.session_state.test_started = False

    if st.session_state.test_started and 'questions' in st.session_state:
        if st.session_state.current < len(st.session_state.questions):
            q = st.session_state.questions[st.session_state.current]
            
            st.progress(st.session_state.current / len(st.session_state.questions))
            st.subheader(f"Вопрос {st.session_state.current + 1} из {len(st.session_state.questions)}")
            st.write(f"**Какой счёт соответствует: {q['name']}?**")
            
            user_answer = st.text_input("Введите номер счёта (например: 10)", key=f"q_{st.session_state.current}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Проверить"):
                    correct = q["number"]
                    if user_answer.strip() == correct:
                        st.success(f"✅ Правильно! Счёт {correct}")
                        st.session_state.score += 1
                    else:
                        st.error(f"❌ Неправильно. Правильный ответ: **{correct}** — {q['name']}")
                    
                    st.session_state.answers.append({
                        "name": q["name"],
                        "user": user_answer.strip(),
                        "correct": correct
                    })
                    st.session_state.current += 1
                    st.rerun()
            
            with col2:
                if st.button("Пропустить"):
                    st.session_state.answers.append({
                        "name": q["name"],
                        "user": "Пропущено",
                        "correct": q["number"]
                    })
                    st.session_state.current += 1
                    st.rerun()
        else:
            # Результаты
            st.success(f"🎉 Тест завершён! Результат: **{st.session_state.score} / {len(st.session_state.questions)}**")
            
            if st.button("Пройти заново"):
                st.session_state.test_started = False
                st.rerun()
            
            st.subheader("Ваши ответы")
            for a in st.session_state.answers:
                status = "✅" if a["user"] == a["correct"] else "❌"
                st.write(f"{status} **{a['name']}** → Ваш ответ: `{a['user']}` | Правильно: `{a['correct']}`")
    else:
        st.info("Выберите настройки в боковой панели и начните тест 👈")

if __name__ == "__main__":
    main()