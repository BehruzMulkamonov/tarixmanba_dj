document.addEventListener("DOMContentLoaded", () => { 
    let selectCategory = document.getElementById("id_category");
    let selectFilterCategory = document.getElementById("id_filter_category");

    // while creating

    selectCategory.addEventListener("change", async (event) => {
        console.log(event.target.value);
        let url = "/api/filter_category/?category=" + event.target.value;
        let response = await fetch(url);
        let status = response.status;
        if (status === 200) {
            let data = await response.json();
            let filterCategoryOptionsHTML = "<option>Select one</option>";
            for (i in data) {
                let filterCategory = data[i];
                console.log(filterCategory);
                filterCategoryOptionsHTML += `<option value="${filterCategory.id}">${filterCategory.title}</option>`;
            }
            selectFilterCategory.innerHTML = filterCategoryOptionsHTML;
        }
    });

    selectFilterCategory.addEventListener("change", async (event) => {
        console.log(event.target.value);
        let url = "/api/filters/?filter_category=" + event.target.value;
        let response = await fetch(url);
        let status = response.status;
        if (status === 200) {
            let data = await response.json();
            let ids = data.map(item => item.id.toString());
            let selectFilters = document.getElementById("id_filters");
            console.log(data);
            console.log(selectFilters);
            selectFilters.childNodes.forEach((child) => {
                console.log(child);
                if (child.nodeName === "OPTION") {
                    let value = child.value;
                    if (ids.includes(value)) {
                        // child.style.visibility = "visible";
                        child.style.display = "block";
                    } else {
                        // child.style.visibility = "hidden";
                        child.style.display = "none";
                    }
                }
            });
        }
    });
});
