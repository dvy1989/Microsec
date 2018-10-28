import * as React from 'react';
import { Table, Form, Row, Col, Label, Input, Button } from 'reactstrap';
import axios, { AxiosResponse } from "axios";

interface ISensor {
  name: string;
  value?: number;
}

interface ISensorListProps {
  onLoadFailed: () => void;
  token: string;
}

interface ISensorListState {
  sensorToAdd: string;
  sensors: ISensor[];
}

export class SensorList extends React.Component<ISensorListProps, ISensorListState>{
  private token: string;
  private onLoadFailed: () => void;
  private wsConnection: WebSocket;

  constructor(props: Readonly<ISensorListProps>) {
    super(props);
    this.onLoadFailed = props.onLoadFailed;
    this.token = props.token;
    this.state = {
      sensorToAdd: "",
      sensors: []
    };
  }

  public componentDidMount() {
    this.wsConnection = new WebSocket("ws://localhost:5001");
    this.wsConnection.onopen = () => {
      console.log("Connected to Web socket");
      this.wsConnection.onmessage = this.handleSocketMessage;
    };
    axios
      .create({
        baseURL: "http://localhost:8000",
        headers: {
          "Accept": "application/json",
          "Authorization": "Token " + this.token,
          "Content-Type": "application/json"
        }
      })
      .get("/api/sensors/")
      .then(this.loadSensorList)
      .catch((error) => console.log(error));
  }

  public render() {
    return (
      <div className="container border rounded p-2">
        <Form className="mb-3">
          <Row>
            <Col sm="2">
              <Label for="sensorname">Sensor name</Label>
            </Col>
            <Col sm="4">
              <Input type="text" name="sensorname" id="sensorname" placeholder="Put sensor name here" defaultValue={this.state.sensorToAdd} onChange={this.onSensorNameChanged} />
            </Col>
            <Col sm="4">
              <Button color="primary" disabled={!this.state.sensorToAdd ? true : false} onClick={this.addSensor}>Add sensor</Button>
            </Col>
          </Row>
        </Form>
        {this.renderSensors()}
      </div>
    );
  }

  private renderSensors(): any {
    if (this.state.sensors) {
      return (
        <Table>
          <thead>
            <tr>
              <th>Sensor name</th>
              <th>Temperature</th>
            </tr>
            {this.renderRows()}
          </thead>
        </Table>
      );
    }
    return <div />;
  }

  private renderRows(): any[] {
    const renders: any[] = [];
    for (const sensor of this.state.sensors) {
      renders.push(
        <tr key={sensor.name}>
          <td>{sensor.name}</td>
          <td>{sensor.value}</td>
        </tr>
      );
    }
    return renders;
  }


  private loadSensorList = (response: AxiosResponse) => {
    if (response.status === 401) {
      this.onLoadFailed();
    }
    else {
      this.setState({ sensors: response.data });
    }
  }

  private onSensorNameChanged = (e: React.FormEvent<HTMLInputElement>) => {
    this.setState({ sensorToAdd: e.currentTarget.value });
  }

  private addSensor = (e: React.FormEvent<HTMLButtonElement>) => {
    axios
      .create({
        baseURL: "http://localhost:8000",
        headers: {
          "Accept": "application/json",
          "Authorization": "Token " + this.token,
          "Content-Type": "application/json"
        }
      })
      .post("/api/sensor/add", { name: this.state.sensorToAdd })
      .catch((error) => console.log(error));
  }

  private handleSocketMessage = (e: MessageEvent) => {
    const messageData = JSON.parse(e.data);
    if (messageData.type === "SENSOR") {
      for (const sensor of this.state.sensors) {
        if (sensor.name === messageData.name) {
          return;
        }
      }
      this.state.sensors.push({ name: messageData.name, value: undefined });
    }
    else if (messageData.type === "VALUE"){
      for (const sensor of this.state.sensors) {
        if (sensor.name === messageData.name) {
          sensor.value = messageData.value;
        }
      }
    }
    this.setState({ sensors: this.state.sensors });
  }
}
