window.addEventListener('load', () => {
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]')
    const deleteBtns = document.querySelectorAll('.delete')

    deleteBtns.forEach(deleteBtn => {
        deleteBtn.addEventListener('click', (e) => {
            e.preventDefault()
            let pk = e.target.getAttribute('href')
            requestDeleteData(pk)

        })
    })


    function requestDeleteData(pk) {
        const url = `/delete/${pk}/`
        const xhr = new XMLHttpRequest();
        xhr.open("POST", url);
        xhr.setRequestHeader('X-CSRFToken', csrfToken.value)
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    location.reload();
                }

            }
        };
        xhr.send();
    }


})