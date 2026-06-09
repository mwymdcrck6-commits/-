import streamlit as st
import random
from typing import List, Dict

# ==================== ДАННЫЕ ПО ПЛАНУ СЧЁТОВ ====================
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
    
    {"number": "19", "name": "НДС по приобретенным ценностям", "type": "А", "section": "НДС"},
    
    {"number": "20", "name": "Основное производство", "type": "А", "section": "Затраты на производство"},
    {"number": "21", "name": "Полуфабрикаты собственного производства", "type": "А", "section": "Затраты на производство"},
    {"number": "23", "name": "Вспомогательные производства", "type": "А", "section": "Затраты на производство"},
    {"number": "25", "name": "Общепроизводственные расходы", "type": "А", "section": "Затраты на производство"},
    {"number": "26", "name": "Общехозяйственные расходы", "type": "А", "section": "Затраты на производство"},
    {"number": "28", "name": "Брак в производстве", "type": "А", "section": "Затраты на производство"},
    {"number": "29", "name": "Обслуживающие производства и хозяйства", "type": "А", "section": "Затраты на производство"},
    
    {"number": "40", "name": "Выпуск продукции", "type": "АП", "section": "Готовая продукция"},
    {"number": "41", "name": "Товары", "type": "А", "section": "Готовая продукция"},
    {"number": "43", "name": "Готовая продукция", "type": "А", "section": "Готовая продукция"},
    {"number": "44", "name": "Расходы на продажу", "type": "А", "section": "Готовая продукция"},
    
    {"number": "50", "name": "Касса", "type": "А", "section": "Денежные средства"},
    {"number": "51", "name": "Расчетные счета", "type": "А", "section": "Денежные средства"},
    {"number": "52", "name": "Валютные счета", "type": "А", "section": "Денежные средства"},
    {"number": "55", "name": "Специальные счета в банках", "type": "А", "section": "Денежные средства"},
    
    {"number": "60", "name": "Расчеты с поставщиками и подрядчиками", "type": "АП", "section": "Расчеты"},
    {"number": "62", "name": "Расчеты с покупателями и заказчиками", "type": "АП", "section": "Расчеты"},
    {"number": "68", "name": "Расчеты по налогам и сборам", "type": "АП", "section": "Расчеты"},
    {"number": "69", "name": "Расчеты по социальному страхованию", "type": "АП", "section": "Расчеты"},
    {"number": "70", "name": "Расчеты с персоналом по оплате труда", "type": "П", "section": "Расчеты"},
    {"number": "71", "name": "Расчеты с подотчетными лицами", "type": "АП", "section": "Расчеты"},
    {"number": "76", "name": "Расчеты с разными дебиторами и кредиторами", "type": "АП", "section": "Расчеты"},
    
    {"number": "80", "name": "Уставный капитал", "type": "П", "section": "Капитал"},
    {"number": "84", "name": "Нераспределенная прибыль (убыток)", "type": "АП", "section": "Капитал"},
    
    {"number": "90", "name": "Продажи", "type": "АП", "section": "Финансовые результаты"},
    {"number": "91", "name": "Прочие доходы и расходы", "type": "АП", "section": "Финансовые результаты"},
    {"number": "99", "name": "Прибыли и убытки", "type": "АП", "section": "Финансовые результаты"},
]

def main():
    st.set_page_config(
        page_title="План счетов — Тест",
        page_icon="🧾",
        layout="centered",
        initial_sidebar_state="collapsed"  # важно для мобильных
    )

    st.title("🧾 Тест по Плану счетов")
    st.markdown("**Бухгалтерский учёт РФ** • Адаптировано для телефона")

    # Боковая панель
    with st.sidebar:
        st.header("Настройки")
        mode = st.radio("Режим теста", ["Случайные вопросы", "По разделу"])
        num_questions = st.slider("Количество вопросов", 5, 30, 10)
        
        if mode == "По разделу":
            sections = sorted(list(set(a["section"] for a in ACCOUNTS)))
            selected_section = st.selectbox("Раздел", sections)
        else:
            selected_section = None

        start_button = st.button("🚀 Начать тест", type="primary", use_container_width=True)

    if start_button or st.session_state.get('test_started', False):
        if 'test_started' not in st.session_state or start_button:
            st.session_state.test_started = True
            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.answers = []
            
            if mode == "По разделу" and selected_section:
                filtered = [acc for acc in ACCOUNTS if acc["section"] == selected_section]
            else:
                filtered = ACCOUNTS.copy()
            
            st.session_state.questions = random.sample(filtered, min(num_questions, len(filtered)))

        if st.session_state.current < len(st.session_state.questions):
            q = st.session_state.questions[st.session_state.current]
            
            progress = st.session_state.current / len(st.session_state.questions)
            st.progress(progress)
            
            st.subheader(f"Вопрос {st.session_state.current + 1} / {len(st.session_state.questions)}")
            st.write(f"**Какой счёт?**")
            st.info(q["name"])
            
            user_answer = st.text_input(
                "Введите номер счёта (например: 51)",
                key=f"input_{st.session_state.current}",
                placeholder="10"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Проверить", use_container_width=True):
                    correct = q["number"]
                    if user_answer.strip() == correct:
                        st.success(f"Правильно! Счёт **{correct}**")
                        st.session_state.score += 1
                    else:
                        st.error(f"Неправильно. Правильный ответ: **{correct}** — {q['name']}")
                    
                    st.session_state.answers.append({
                        "name": q["name"], "user": user_answer.strip(), "correct": correct
                    })
                    st.session_state.current += 1
                    st.rerun()
            
            with col2:
                if st.button("⏭ Пропустить", use_container_width=True):
                    st.session_state.answers.append({
                        "name": q["name"], "user": "Пропущено", "correct": q["number"]
                    })
                    st.session_state.current += 1
                    st.rerun()
        else:
            # Финальный результат
            st.success(f"🎉 Тест завершён!\n**Результат: {st.session_state.score} из {len(st.session_state.questions)}**")
            
            if st.button("🔄 Пройти заново", use_container_width=True):
                st.session_state.test_started = False
                st.rerun()
            
            st.subheader("Результаты")
            for a in st.session_state.answers:
                emoji = "✅" if a["user"] == a["correct"] else "❌"
                st.write(f"{emoji} **{a['name']}** → `{a['user']}` | Правильно: `{a['correct']}`")
    else:
        st.info("👈 Откройте боковое меню (кнопка вверху слева) и нажмите «Начать тест»")

if __name__ == "__main__":
    main()