%include base_template

<style>
    .singleArticle{
        background: #f0f0f0;
        width: 70%;
        height: 75%;
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
        font-size: 10px
        margin: 10px 0px 10px 0px;
    }

    .articleTitle{
        display: flex;
        justify-content: center;
        align-items: center;
        border-bottom: 3px solid black;
    }

    .articleTitle h1{
        color: black;
    }

    .articleBody{
        display: flex;
        margin: 20px;
    }

    .articleBody p{
        color: black;
    }
</style>

<div class="main">
    <h1> viewing: {{mode}} </h1>

    <div class="singleArticle">
        <div class="articleAuthor">
            <h4>author: {{article_author}} - {{article_date}}</h4>
        </div>

        <div class="articleTitle">
            <h1>{{article_title}}</h1>
        </div>

        <div class="articleBody">
            <p>{{article_body}}</p>
        </div>
    </div>
</div>