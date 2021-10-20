window.addEventListener('load', ()=>{
    const order = document.querySelector('#order')
    const schemeColumns = document.querySelector('#scheme-columns')
    const schemeFormAdd = document.querySelector('#scheme-form-add')
    const type = document.querySelector('#type')
    const columnName = document.querySelector('#column-name')
    const btnAddScheme = document.querySelector('#add-scheme')
    const schemeName = document.querySelector('#scheme-name')
    const btnSubmitScheme = document.querySelector('#submit-scheme')
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]')

    let currentItemId = 0
    let isFirstItemAdded = true



    btnAddScheme.addEventListener('click', ()=>{
         const orderValue = order.value
         const typeValue = type.value
         const typeSelectedIndex = type.selectedIndex
        console.log(typeValue)
         const columnNameValue = columnName.value

        if (orderValue===''||columnNameValue===''){
            alert('Enter all fields')
            return
        }

        if (isNaN(orderValue)){
            alert('Order must be index number!')
            return
        }


        schemeColumns.innerHTML+="<form class=\"w-50 text-center m-auto\">\n" +
            "<fieldset disabled>  " +
            "<div class=\"form-group d-inline-block\">\n" +
            `    <label for=\"column-name-${currentItemId}\">Column name</label>\n` +
            `    <input value=\"${columnNameValue}\" type=\"text\" class=\"form-control column-name\" id=\"column-name-${currentItemId}\">\n` +
            "  </div>\n" +
            "\n" +
            "  <div class=\"form-group d-inline-block\">\n" +
            `    <label for=\"type-${currentItemId}\">Type</label>\n` +
            `    <select class=\"form-control type\" id=\"type-${currentItemId}\">\n` +
            "        \n" +
             `           <option>${typeValue}</option>\n` +

            "\n" +
            "    </select>\n" +
            "  </div>\n" +
            "     <div class=\"form-group d-inline-block \">\n" +
            `    <label for=\"order-${currentItemId}\">Order</label>\n` +
            `   <input value=\"${orderValue}\" type=\"text\" class=\"form-control order\" id=\"order-${currentItemId}\">\n` +
            "   </div>\n" +

            "</fieldset>"+
            "</form>"
        currentItemId+=1
        type.remove(typeSelectedIndex)
        if (type.value===''){
            schemeFormAdd.classList.add('d-none')
        }
         if (isFirstItemAdded===true){
            btnSubmitScheme.classList.remove('d-none')
         isFirstItemAdded= false
    }

    })

    btnSubmitScheme.addEventListener('click', ()=>{




        const schemeNameValue = schemeName.value
        if (schemeNameValue===''){
            alert('Enter Scheme Name')
            return
        }



        let  queryItems = {
            'scheme_name':schemeNameValue,
            'scheme_columns':[],
            }

        const orderList = document.querySelectorAll('.order')
        const columnNameList = document.querySelectorAll('.column-name')
        const typeList = document.querySelectorAll('.type')
        orderList.forEach((_, index) =>
            {
                queryItems['scheme_columns'].push({
                    'column_name':columnNameList[index].value,
                    'order':orderList[index].value,
                    'type':typeList[index].value
                })
            })

        queryItems = JSON.stringify(queryItems)
         requestSendData(queryItems)



    })


    function requestSendData(data){
        // var url = "https://reqbin.com/echo/post/json";
        const url = document.location.href

        let xhr = new XMLHttpRequest();
        xhr.open("POST", url);
        xhr.setRequestHeader('X-CSRFToken',csrfToken.value)
        xhr.setRequestHeader("Accept", "application/json");
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
           if (xhr.readyState === 4) {

              if (xhr.status===200){
                  document.location.href = document.location.origin
              }

           }};



        xhr.send(data);
            }


})