---
layout: default
title: News
permalink: /pages/news/
nav_order: 1
---

News
====

News, observations, and thoughts about Teochew language and this website.

Blog posts are cross-posted from our [Facebook page](https://facebook.com/learnteochew),
so you may see statements about leaving comments or following our Page. If you
use Facebook, do follow us there for update notifications!

If you use a feed reader, you can subscribe to posts via our
[Atom feed]({{ site.baseurl }}{% link feed.xml %}).

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
