// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded affix "><a href="index.html">Титульна сторінка</a></li><li class="chapter-item expanded "><a href="intro/index.html"><strong aria-hidden="true">1.</strong> Вступ</a></li><li class="chapter-item expanded "><a href="requirements/index.html"><strong aria-hidden="true">2.</strong> Розроблення загальних вимог до системи</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="requirements/state-of-the-art.html"><strong aria-hidden="true">2.1.</strong> Аналіз предметної області</a></li><li class="chapter-item expanded "><a href="requirements/stakeholders-needs.html"><strong aria-hidden="true">2.2.</strong> Запити зацікавлених осіб</a></li></ol></li><li class="chapter-item expanded "><a href="use_cases/index.html"><strong aria-hidden="true">3.</strong> Розроблення функціональних вимог до системи</a></li><li class="chapter-item expanded "><a href="design/index.html"><strong aria-hidden="true">4.</strong> Проєктування інформаційного забезпечення</a></li><li class="chapter-item expanded "><a href="software/index.html"><strong aria-hidden="true">5.</strong> Реалізація інформаційного та програмного забезпечення</a></li><li class="chapter-item expanded "><a href="test/index.html"><strong aria-hidden="true">6.</strong> Тестування працездатності системи</a></li><li class="chapter-item expanded "><a href="conclusion/index.html"><strong aria-hidden="true">7.</strong> Висновки</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString();
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
