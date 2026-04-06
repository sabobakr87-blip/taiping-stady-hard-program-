import webview
import threading
import time

# الرابط الرئيسي لموقعك
HOME_URL = 'https://sabobakr87-blip.github.io/taiping-stady-hard/'

def add_custom_button(window):
    """هذه الدالة تضع الزرار بين البحث وكلمة تايبينج"""
    while True:
        script = """
        if (!document.getElementById('home-back-btn')) {
            var btn = document.createElement('button');
            btn.id = 'home-back-btn';
            btn.innerHTML = '🏠 الرئيسية';
            btn.style.position = 'fixed';
            btn.style.top = '12px';      /* ضبط الارتفاع ليكون موازي للمربع */
            btn.style.left = '550px';    /* المسافة من اليسار ليأتي بعد مربع البحث */
            btn.style.zIndex = '999999';
            btn.style.padding = '10px 12px';
            btn.style.fontSize = '12px';  /* تصغير الخط ليناسب المساحة */
            btn.style.backgroundColor = '#10a37f';
            btn.style.color = 'white';
            btn.style.border = 'none';
            btn.style.borderRadius = '20px'; /* جعل الحواف دائرية مثل مربع البحث */
            btn.style.cursor = 'pointer';
            btn.style.fontWeight = 'bold';
            
            btn.onclick = function() { window.location.href = 'https://sabobakr87-blip.github.io/taiping-stady-hard/'; };
            document.body.appendChild(btn);
        }
        """
        try:
            window.evaluate_js(script)
        except:
            pass
        import time
        time.sleep(1)


def run_app():
    # إنشاء نافذة التطبيق
    window = webview.create_window(
        'Taiping Study Hard', 
        HOME_URL,
        width=1200,
        height=800
    )

    # تشغيل خيط (Thread) جانبي لمراقبة الصفحة وإضافة الزرار
    threading.Thread(target=add_custom_button, args=(window,), daemon=True).start()

    webview.start()

if __name__ == '__main__':
    run_app()
