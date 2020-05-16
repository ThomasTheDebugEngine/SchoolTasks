%include base_template

<style>
    .singleArticle{
        background: #f0f0f0;
        width: 70%;
        height: fit-content;
        margin: auto;
        display: flex;
        flex-direction: column;
    }

    .articleAuthor{
        padding-left: 10px;
        display: flex;
        align-items: center;
        border-bottom: 3px solid black;
    }

    .articleAuthor h4{
        color: orange;
        font-size: 20px;
        margin: 10px 0px 10px 0px;
    }

    .comment{
        background: #f0f0f0;
        padding: 5px;
        margin: auto;
        margin-top: 10px;
        width: 70%;
        height: fit-content;
    }

    .comment p{
        color: black;
        margin: 5px 5px;
    }

</style>

<div class="main">
    <h1> viewing: {{mode}} </h1>

    <div class="singleArticle">
        <div class="articleAuthor">
            <h4>author: {{article_author}} - {{article_date}} - title: {{article_title}}</h4>
        </div>
    </div>
<div>

<div class="commentContainer">
    %for index in range(0, comment_list_length):
        <div class="comment">
            <p>
                <span style="color: blue"> {{comment_email_list[index]}} - {{comment_time_list[index]}} </span>
                says: {{comment_body_list[index]}}</p>
        </div>
</div>