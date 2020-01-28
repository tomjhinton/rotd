import React from 'react'
import axios from 'axios'







class Main extends React.Component{
  constructor(props){
    super(props)
    this.state = {
      data: {},



    }
    this.componentDidMount = this.componentDidMount.bind(this)


  }

  componentDidMount(){

    axios.get('/api/records')
      .then(res => this.setState({record: res.data}))




  }

  componentDidUpdate(prevProps){

  }





  render() {

    console.log(this.state)
    return (
      <div className='container'>

      Hiya
      </div>






    )
  }
}
export default Main
