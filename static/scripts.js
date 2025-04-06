// 显示/隐藏返回顶部按钮
window.onscroll = function() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        document.getElementById("scrollToTop").style.display = "block";
    } else {
        document.getElementById("scrollToTop").style.display = "none";
    }
};