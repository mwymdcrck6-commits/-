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
    {"number": "12", "name": "Малоценные и быстроизнашивающиеся предметы", "type": "А", "section": "Производственные запасы"},
    {"number": "14", "name": "Резервы под снижение стоимости материальных ценностей", "type": "П", "section": "Производственные запасы"},
    {"number": "15", "name": "Заготовление и приобретение материальных ценностей", "type": "А", "section": "Производственные запасы"},
    {"number": "16", "name": "Отклонение в стоимости материальных ценностей", "type": "АП", "section": "Производственные запасы"},
    {"number": "20", "name": "Основное производство", "type": "А", "section": "Затраты на производство"},
    {"number": "21", "name": "Полуфабрикаты собственного производства", "type": "А", "section": "Затраты на производство"},
    {"number": "23", "name": "Вспомогательные производства", "type": "А", "section": "Затраты на производство"},
    {"number": "25", "name": "Общепроизводственные расходы", "type": "А", "section": "Затраты на производство"},
    {"number": "26", "name": "Общехозяйственные расходы", "type": "А", "section": "Затраты на производство"},
    {"number": "28", "name": "Брак в производстве", "type": "А", "section": "Затраты на производство"},
    {"number": "29", "name": "Обслуживающие производства и хозяйства", "type": "А", "section": "Затраты на производство"},
    {"number": "50", "name": "Касса", "type": "А", "section": "Денежные средства"},
    {"number": "51", "name": "Расчетные счета", "type": "А", "section": "Денежные средства"},
    {"number": "52", "name": "Валютные счета", "type": "А", "section": "Денежные средства"},
    {"number": "55", "name": "Специальные счета в банках", "type": "А", "section": "Денежные средства"},
    {"number": "57", "name": "Переводы в пути", "type": "А", "section": "Денежные средства"},
    {"number": "60", "name": "Расчеты с поставщиками и подрядчиками", "type": "АП", "section": "Расчеты"},
    {"number": "62", "name": "Расчеты с покупателями и заказчиками", "type": "АП", "section": "Расчеты"},
    {"number": "66", "name": "Расчеты по краткосрочным кредитам и займам", "type": "П", "section": "Расчеты"},
    {"number": "68", "name": "Расчеты по налогам и сборам", "type": "АП", "section": "Расчеты"},
    {"number": "69", "name": "Расчеты по социальному страхованию и обеспечению", "type": "АП", "section": "Расчеты"},
    {"number": "70", "name": "Расчеты с персоналом по оплате труда", "type": "П", "section": "Расчеты"},
    {"number": "73", "name": "Расчеты с персоналом по прочим операциям", "type": "АП", "section": "Расчеты"},
    {"number": "76", "name": "Расчеты с разными дебиторами и кредиторами", "type": "АП", "section": "Расчеты"},
    {"number": "80", "name": "Уставный капитал", "type": "П", "section": "Капитал"},
    {"number": "81", "name": "Собственные акции (доли)", "type": "А", "section": "Капитал"},
    {"number": "83", "name": "Добавочный капитал", "type": "П", "section": "Капитал"},
    {"number": "84", "name": "Нераспределенная прибыль (непокрытый убыток)", "type": "АП", "section": "Капитал"},
    {"number": "90", "name": "Продажи", "type": "АП", "section": "Финансовые результаты"},
    {"number": "91", "name": "Прочие доходы и расходы", "type": "АП", "section": "Финансовые результаты"},
    {"number": "94", "name": "Недостачи и потери от порчи ценностей", "type": "А", "section": "Финансовые результаты"},
    {"number": "99", "name": "Прибыли и убытки", "type": "АП", "section": "Финансовые результаты"}
]

def main():
    st.set_page_config(
        page_title="План счетов — Тест",
        page_icon="🧾",
        layout="centered",  # Адаптация макета под мобильное устройство
        initial_sidebar_state="collapsed"
    )

    st.title("🧾 Тест: План счетов")
    st.caption("Приказ Минфина РФ № 94н • Полный список счетов")

    tab1, tab2 = st.tabs(["🧪 Тест", "📖 Справочник"])

    with tab1:
        with st.sidebar:
            st.header("Настройки теста")
            mode = st.radio("Тип вопросов", ["Ввод номера", "Выбор варианта"])
            num_questions = st.slider("Вопросы", 5, 20, 10)

            if st.button("🚀 Начать"):
                st.session_state.test_started = True
                st.session_state.current = 0
                st.session_state.score = 0

                st.session_state.questions = random.sample(ACCOUNTS, num_questions)
                st.rerun()

        if st.session_state.get('test_started', False):
            if st.session_state.current < len(st.session_state.questions):
                q = st.session_state.questions[st.session_state.current]

                st.subheader(f"Вопрос {st.session_state.current + 1} из {len(st.session_state.questions)}")
                st.info(f"**{q['name']}**")

                if mode == "Ввод номера":
                    user_answer = st.text_input("Введите номер", placeholder="01")
                    if st.button("Проверить"):
                        if user_answer.strip() == q['number']:
                            st.success(f"✅ Верно! Номер: {q['number']}")
                            st.session_state.score += 1
                        else:
                            st.error(f"❌ Неверно. Правильный номер: {q['number']}")

                        st.session_state.current += 1
                        st.rerun()
                else:
                    options = [q["number"]] + random.sample(
                        [a["number"] for a in ACCOUNTS if a != q], 3
                    )
                    random.shuffle(options)

                    for opt in options:
                        if st.button(opt):
                            if opt == q["number"]:
                                st.success("✅ Верно!")
                                st.session_state.score += 1
                            else:
                                st.error(f"❌ Неверно! Правильный ответ: {q['number']}")

                            st.session_state.current += 1
                            st.rerun()
            else:
                st.success(f"Тест завершён! Ваш результат: {st.session_state.score} из {len(st.session_state.questions)}")
                if st.button("Новый тест"):
                    st.session_state.test_started = False
                    st.rerun()

    with tab2:
        st.subheader("📖 Справочник")
        for acc in ACCOUNTS:
            st.write(f"**{acc['number']}** — {acc['name']} ({acc['type']}) • {acc['section']}")

if __name__ == "__main__":
    main()