window.addEventListener('load', () => {
    const btnGenerateRows = document.querySelector('#btn-generate-rows')
    const rowsToBeGenerated = document.querySelector('#rows')
    const datasetName = document.querySelectorAll('.scheme-name')
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]')
    const datasetStatus = document.querySelectorAll('.dataset-status')
    const tds = document.querySelectorAll("td[class=scheme-name]")
    const downloadLinks = document.querySelectorAll(".download")

    console.log(downloadLinks)


    downloadLinks.forEach(link => {
        if (link.innerHTML === 'Download') {
            let dataSetStatus = link.parentElement.parentElement.querySelector('.dataset-status')
            dataSetStatus.className = 'dataset-status bg-success text-light'
            dataSetStatus.innerHTML = 'Ready'
        }
        else {
            let dataSetStatus = link.parentElement.parentElement.querySelector('.dataset-status')
            dataSetStatus.className = 'dataset-status bg-secondary text-light'
            dataSetStatus.innerHTML = 'Processing'
        }
    })


    let isIntervalStarted = false
    console.log(datasetName)

    console.log(btnGenerateRows)
    console.log(rowsToBeGenerated)
    let data = {'rows': 0, 'scheme_names': []}

    function removePreviousColor() {
        datasetStatus.forEach(item => {
            item.className = 'dataset-status'
        })

    }

    function changeCurrentItemStatusToReady(status) {
        status.className = 'dataset-status bg-success text-light'
        status.innerHTML = 'Ready'
    }



    function clearDownloadLinks() {
        downloadLinks.forEach(link => {
            link.innerHTML = ''
            link.setAttribute('href', '')
        })
    }


    function changeStatusToProcessing() {
        removePreviousColor()
        datasetStatus.forEach(item => {
            item.className = 'dataset-status bg-secondary text-light'
            item.innerHTML = 'Processing'
        })

    }


    datasetName.forEach(element => {
            let dataItem = element.innerHTML
            data['scheme_names'].push(dataItem)
        }
    )

    function startInterval() {
        if (isIntervalStarted === false) {
            setInterval(requestUpdateDownloadStatus, 1000)
            isIntervalStarted = true
        }
    }


    btnGenerateRows.addEventListener('click', () => {

        if (rowsToBeGenerated.value.match(/\d+/g)) {
            data['rows'] = rowsToBeGenerated.value

            changeStatusToProcessing()
            clearDownloadLinks()
            requestSendData(data)
            startInterval()
            console.log(data)


        }
    })


    function requestUpdateDownloadStatus() {
        const url = '/get_download_status'
        console.log(url)
        const xhr1 = new XMLHttpRequest();
        xhr1.open("GET", url);

        xhr1.onreadystatechange = function () {
            if (xhr1.readyState === 4) {
                if (xhr1.status === 200) {
                    data = JSON.parse(xhr1.responseText)
                    console.log(data)

                    tds.forEach(td => {
                        let download_link = td.parentNode.querySelector('a')
                        data.forEach(item => {

                            if (item['scheme_name'] === td.innerHTML) {

                                if (item['status'] === 1) {

                                    let download_link = td.parentNode.querySelector('a')
                                    let status = td.parentNode.querySelector('.dataset-status')
                                    download_link.setAttribute('href', item['download_link'])
                                    download_link.innerHTML = 'Download'
                                    changeCurrentItemStatusToReady(status)

                                } else {
                                    console.log('Not ready yet')
                                    let download_link = td.parentNode.querySelector('a')
                                    download_link.innerHTML = ''
                                }
                            }
                        })

                    })


                    // data.forEach(item => {
                    //     if (item['status'] === 1) {
                    //         tds.forEach(td => {
                    //             let schemeNameTd = td.innerHTML
                    //             if (schemeNameTd === item['scheme_name']) {
                    //                 if (item['status'] === 1) {
                    //
                    //                     let download_link = td.parentNode.querySelector('a')
                    //                     download_link.setAttribute('href', item['download_link'])
                    //
                    //                     download_link.value = 'Download'
                    //
                    //                 }
                    //                 else{
                    //                     console.log('Not ready yet')
                    //                     let download_link = td.parentNode.querySelector('a')
                    //                     download_link.value = ''
                    //                 }
                    //
                    //
                    //
                    //             }
                    //         })
                    //     }
                    //
                    // })
                    //

                    // document.location.href = document.location.origin
                }

            }
        };


        xhr1.send(data);
    }


    function requestSendData(data) {
        data = JSON.stringify(data)
        const url = document.location.href

        const xhr = new XMLHttpRequest();
        xhr.open("POST", url);
        xhr.setRequestHeader('X-CSRFToken', csrfToken.value)
        xhr.setRequestHeader("Accept", "application/json");
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {

                if (xhr.status === 200) {
                    // document.location.href = document.location.origin
                }

            }
        };


        xhr.send(data);
    }
})