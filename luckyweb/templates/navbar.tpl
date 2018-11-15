<nav class="navbar navbar-expand-md bg-dark navbar-dark">
  <!-- Brand -->
  <a class="navbar-brand" href="{{ args.li_list[0].href }}">{{ args.li_list[0].text }}</a>
 
  <!-- Toggler/collapsibe Button -->
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
 
  <!-- Navbar links -->
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      {% for li in args.li_list[1:] %}
	    {% if li.get('active') %}
        <li class="nav-item active">
		{% else %}
        <li class="nav-item">
		{% endif %}
          <a href="{{ li.href }}" class="nav-link">{{ li.text }}</a>
        </li>
      {% endfor %}
    </ul>
  </div> 
</nav>
