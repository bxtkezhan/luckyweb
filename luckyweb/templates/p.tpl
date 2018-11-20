{% if lead|not %}
<p class="" >{{ text }}</p>
{% endif %}
{% if lead %}
<p class="lead" >{{ text }}</p>
{% endif %}
