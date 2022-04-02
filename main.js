const modal_wrapper = document.querySelector('.modals-wrapper');
if (modal_wrapper) {
    function display_modal(modal_id) {
        const modal = document.getElementById(modal_id);
        modal.style.display = "flex";
        modal_wrapper.style.display = "flex";

        const close_button = document.getElementById("close-modal");
        close_button.addEventListener('click', () => {
            modal.style.display = "none";
            modal_wrapper.style.display = "none";
        })
    }
}