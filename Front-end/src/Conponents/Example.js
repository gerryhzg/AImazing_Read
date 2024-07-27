import React from 'react'
import "./Example.css"
import { IoSettingsSharp } from "react-icons/io5";

export default function Example() {
  return (
    <div className='Example_Main_Div'>

        <div className='Card_Div bc1'>

            <label className='title'>Input an Article</label>

            <div className='FakeInput_Div'>
                <label>A transformer is a deep learning architecture developed by Google and based on the multi-head attention mechanism, proposed in a 2017 paper </label>
                <p>"Attention Is All You Need".</p>
            </div>

        </div>

        <div className='Card_Div bc2'>

            <label className='title'>AI model</label>

            <div className='row_div'>
                <div className='colomn_div'>
                    <label>Summarize</label>
                    <label>Image</label>
                    <label>Voice</label>
                    <label>Music</label>
                </div>
                <IoSettingsSharp className='icon'/>
            </div>

            {/* <label className='detail' >ChatGPT</label>
            <label className='detail'>Dalle</label> */}

        </div>

        <div className='Card_Div bc3'>
            <label className='title'>Story For Kids</label>
            <div className='image_div'>
                <img src={require('../Media/1.png')}/>
                <img src={require('../Media/2.png')}/>
                <img src={require('../Media/3.png')}/>
            </div>
        </div>

    </div>
  )
}
