{% if not args.get('lead') %}
<p class="" >{{ args.text }}</p>
{% else %}
<p class="lead" >{{ args.text }}</p>
{% endif %}
