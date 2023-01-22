// 15:44

document.addEventListener("DOMContentLoaded", function(){
    scheduler.i18n.setLocale("fr")
    scheduler.plugins({
        limit:true,
        year_view: true,
        minical: true
    });

    scheduler.locale.labels.year_tab ="Année";

    scheduler.config.first_hour = 7;
    scheduler.config.last_hour = 21;
    scheduler.config.readonly = true;

    scheduler.attachEvent("onDataRender", function(){
        scheduler.markTimespan({  
            days:  [0,1,2,3,4,5,6],               // marks each Friday  
            zones: [7*60,8*60,13*60,14*60,20*60,21*60],
            css:   "medium_lines_section"   // the applied css style
        });
    });

    scheduler.init('schedulerEnac');


    

    scheduler.render()

    // Filtrage

    document.querySelector('select#filtre').addEventListener('change',function(event){
        let select_filtre = document.querySelector("select#filtre")
        let value = select_filtre.options[select_filtre.selectedIndex].value

        function est_dans(mot,txt) {
            var result=txt.search(mot)
            if (result>=0) {
                return true
            }
            else {
                return false
            }
            
        }

        // alert(est_dans('TDP:0','MVT:10 TDP:0 !'))


            scheduler.filter_week = function(id, event){
                if(est_dans('TDP:0',event.text) & value=='tdp') {return true}
                else if(!est_dans('TDP:0',event.text) & value=='mvt') {return true}
                else if (value=='both') {return true}
                else { return false}
            }

            scheduler.filter_day = function(id, event){
                if(est_dans('TDP:0',event.text) & value=='tdp') {return true}
                else if (value=='both') {return true}
                else { return false}
            }

            scheduler.filter_month = function(id, event){
                if(est_dans('TDP:0',event.text) & value=='tdp') {return true}
                else if (value=='both') {return true}
                else { return false}
            }
    
    scheduler.render();
    })

    

    
    
    



    // Fin Filtrage






   fetch('/getCalendar', {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
    })
    .then((res) => res.json())
    .then((data) => {
        scheduler.parse(data,"json");
    })
    .catch((err) => console.log(err))
}
)


function show_minical(){
    if (scheduler.isCalendarVisible()){
        scheduler.destroyCalendar();
    } else {
        scheduler.renderCalendar({
            position:"dhx_minical_icon",
            date:scheduler._date,
            navigation:true,
            handler:function(date,calendar){
                scheduler.setCurrentView(date);
                scheduler.destroyCalendar()
            }
        });
    }
}
