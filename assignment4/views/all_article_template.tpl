
%include base_template

<style>
    .allArticles{
        background: red;
    }

    .article{
        background: #f0f0f0;
        margin: 10px 0px;
        padding: 1px 5px;
        display: flex;
    }

    .articleAuthor p{
        color: orange;
    }

    .articleTitle p{
        color: black;
    }
</style>

<div class="main">
    <h1> viewing: {{mode}} </h1>

     <div class="allArticles">
        %for index in range(0, articles_list_length):
            <div class="article" onclick="window.location = '/articles/{{index + 1}}/comments';">
                <div class="articleAuthor">
                    <p> author: {{authors_list[index]}} - {{times_list[index]}} </p>
                </div>

                <div class="articleTitle">
                    <p>, title: {{title_list[index]}}</p>
                </div>
            </div>
     </div>
</div>