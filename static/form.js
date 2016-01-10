function get_ships(ship_count) {
        var number = ship_count;
        var f = document.createElement("form");
        f.setAttribute('method', "post");
        f.setAttribute('action', "submit");
        for (i = 0; i < number; i++) {
                var e = document.createElement("input"); //input element, text
                e.setAttribute('type', "text");
                e.setAttribute('name', "Name" + i);
                var g = document.createElement("input"); //input element, text
                e.setAttribute('type', "text");
                e.setAttribute('name', "Mass" + i);
                var h = document.createElement("input");
                e.setAttribute('type', "checkbox");
                e.setAttribute('name', "mwd" + i);
                f.innerHTML = f.innerHTML + "<br />Name: ";
                f.appendChild(h);
                f.innerHTML = f.innerHTML + "<br />Mass: ";
                f.appendChild(g);
                f.innerHTML = f.innerHTML + "<br />Has MWD? ";
                f.appendChild(e);
                f.innerHTML = f.innerHTML + "<br /><br />";
        }
        var s = document.createElement("input"); //input element, Submit button
        s.setAttribute('type', "submit");
        s.setAttribute('value', "Submit");
        f.appendChild(s);
        document.getElementsByName('container')[0].appendChild(f);
}
get_ships(2);
