document.addEventListener('DOMContentLoaded', () => {
    const languageSelector = document.getElementById('language-selector');
    const faqList = document.getElementById('faq-list');

    const fetchFAQs = async (lang = 'en') => {
        try {
            const response = await fetch(`/api/faqs/?lang=${lang}`);
            const data = await response.json();

            faqList.innerHTML = '';

            if (data.length === 0) {
                faqList.innerHTML = '<p class="text-center">No FAQs available.</p>';
                return;
            }

            data.forEach(faq => {
                const faqItem = document.createElement('div');
                faqItem.classList.add('faq-item', 'col-md-12');
                faqItem.innerHTML = `
                    <h5>${faq.question}</h5>
                    <p>${faq.answer}</p>
                `;
                faqList.appendChild(faqItem);
            });
        } catch (error) {
            console.error('Error fetching FAQs:', error);
            faqList.innerHTML = '<p class="text-center text-danger">Failed to load FAQs.</p>';
        }
    };

    fetchFAQs();

    languageSelector.addEventListener('change', (event) => {
        const selectedLang = event.target.value;
        fetchFAQs(selectedLang);
    });
});