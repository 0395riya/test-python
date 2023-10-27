import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import { Card, Col, Row } from 'react-bootstrap';

// import Data from './Data';

function App() {
  const [list, setList] = useState([])

  const url = "https://dummy.restapiexample.com/api/v1/employees";

  const getApi = async (url) => {
    await axios.get(url).then((res) => {
      setList(res.data.data)
      console.log(res.data.data);
    })
  }

  useEffect(() => {
    getApi(url)
  }, [])


  return (
    <div className='App'>

      <Row xs={1} md={2} className="g-4 container">
        {list.length > 0 && list.map((item, index) => {



          return (

            <Col key={index}>
              <Card border="warning" style={{ width: '18rem', display: 'inline-flex' }}>

                <Card.Body>
                  <Card.Title>{item.id} {" : "} {item.employee_name}</Card.Title>
                  <Card.Text>
                    <p>Age :{" "}{item.employee_age}</p>
                    <p>Salary :{" "}{item.employee_salary}</p>
                  </Card.Text>
                </Card.Body>
              </Card>
            </Col>
          )
        })}
        {/* <Data/> */}
      </Row>
    </div>
  );
}

export default App;
