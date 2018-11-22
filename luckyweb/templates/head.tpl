{% if display_num %}
  {% if center|not %}
<h{{ head_num }} class="display-{{ display_num }}" >{{ text }}</h{{ head_num }}>
  {% else %}
<h{{ head_num }} class="display-{{ display_num }}" ><center>{{ text }}</center></h{{ head_num }}>
  {% endif %}
{% else %}
  {% if center|not %}
<h{{ head_num }} class="" >{{ text }}</h{{ head_num }}>
  {% else %}
<h{{ head_num }} class="" ><center>{{ text }}</center></h{{ head_num }}>
  {% endif %}
{% endif %}
