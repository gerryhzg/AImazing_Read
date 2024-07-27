import React,{useState} from 'react'
import "./Book.css"
export default function Book() {
    const [BooksData,SetBooksData] = useState([
        {
            PageImage:"1.png",
            Content:"A transformer is a deep learning architecture developed by Google and based on the multi-head attention mechanism, proposed in a 2017 paper 'Attention Is All You Need'."
        },
        {
            PageImage:"2.png",
            Content:"A transformer is a deep learning architecture developed by Google and based on the multi-head attention mechanism, proposed in a 2017 paper 'Attention Is All You Need'."
        }
    ])

    const [CurrentPage,SetCurrentPage] = useState(0)

  return (
    <div className='Book_Main_Div'>

        <div className='Content_Div'>
            {
                BooksData[CurrentPage] && 
                <img src={require(`../Media/${BooksData[CurrentPage].PageImage}`)} />
            }
            <div className='Text_Content'>
                <p>
                    {BooksData[CurrentPage].Content}
                </p>
            </div>
        </div>

        <div className='Control_Div'>
            <button>Back</button>
            <button>Next Page</button>
        </div>

    </div>
  )
}
